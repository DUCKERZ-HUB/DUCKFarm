import re
import sys
import threading
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import start_sploit as runner


class FlagStorageTests(unittest.TestCase):
    def setUp(self):
        self.old_storage = runner.flag_storage
        self.old_exit_event = runner.exit_event
        runner.flag_storage = runner.FlagStorage()
        runner.exit_event = threading.Event()

    def tearDown(self):
        runner.flag_storage = self.old_storage
        runner.exit_event = self.old_exit_event

    def test_queue_deduplicates_and_wakes_consumer(self):
        storage = runner.flag_storage
        storage.add(['A', 'B', 'A'], 'Team')
        self.assertTrue(storage.wait_for_flags(0))
        self.assertEqual([item['flag'] for item in storage.pick_flags(2)], ['A', 'B'])
        storage.mark_as_sent(1)
        storage.add(['A', 'B'], 'Team')
        self.assertEqual(storage.queue_size, 1)
        storage.mark_as_sent(1)
        self.assertFalse(storage.wait_for_flags(0))

    def test_successful_batches_drain_without_waiting(self):
        storage = runner.flag_storage
        storage.add((str(i) for i in range(25001)), 'Team')
        sizes = []

        def post(_args, batch):
            sizes.append(len(batch))
            if sum(sizes) == 25001:
                runner.exit_event.set()

        with patch.object(runner, 'post_flags', side_effect=post):
            runner.run_post_loop(SimpleNamespace())

        self.assertEqual(sizes, [10000, 10000, 5001])
        self.assertEqual(storage.queue_size, 0)

    def test_failed_post_retries_same_flags(self):
        runner.flag_storage.add(['A'], 'Team')
        batches = []

        def post(_args, batch):
            batches.append([item['flag'] for item in batch])
            if len(batches) == 1:
                raise RuntimeError('temporary failure')
            runner.exit_event.set()

        with patch.object(runner, 'post_flags', side_effect=post), \
                patch.object(runner, 'POST_PERIOD', 0.001):
            runner.run_post_loop(SimpleNamespace())

        self.assertEqual(batches, [['A'], ['A']])
        self.assertEqual(runner.flag_storage.queue_size, 0)

    def test_http_413_halves_batch_without_losing_flags(self):
        runner.flag_storage.add((str(i) for i in range(12000)), 'Team')
        attempted = []
        delivered = []

        def post(_args, batch):
            attempted.append(len(batch))
            if len(batch) > 5000:
                raise runner.PayloadTooLarge('HTTP 413')
            delivered.extend(item['flag'] for item in batch)
            if len(delivered) == 12000:
                runner.exit_event.set()

        with patch.object(runner, 'post_flags', side_effect=post):
            runner.run_post_loop(SimpleNamespace())

        self.assertEqual(attempted, [10000, 5000, 5000, 2000])
        self.assertEqual(len(set(delivered)), 12000)
        self.assertEqual(runner.flag_storage.queue_size, 0)

    def test_http_413_response_is_classified(self):
        args = SimpleNamespace(
            sploit='test.py', server_url='http://127.0.0.1:5137', server_pass='test'
        )
        with patch.object(runner.requests, 'post') as post:
            post.return_value.status_code = 413
            post.return_value.ok = False
            with self.assertRaises(runner.PayloadTooLarge):
                runner.post_flags(args, [{'flag': 'A', 'team': '*'}])

    def test_nonverbose_output_does_not_display_but_posts_flags(self):
        class Stream:
            def __init__(self):
                self.lines = iter([b'A' * 31 + b'=\n', b''])

            def readline(self):
                return next(self.lines)

        args = SimpleNamespace(verbose_attacks=0, endless=False)
        with patch.object(runner, 'display_sploit_output') as display:
            runner.process_sploit_output(
                Stream(), args, 'Team', re.compile(r'[A-Z0-9]{31}='), 1
            )
        display.assert_not_called()
        self.assertEqual(runner.flag_storage.queue_size, 1)


if __name__ == '__main__':
    unittest.main()
