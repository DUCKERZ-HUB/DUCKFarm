# DUCKFarm

This is a fork of [S4DFarm](https://github.com/C4T-BuT-S4D/S4DFarm) which is fork of [DestructiveFarm](https://github.com/DestructiveVoice/DestructiveFarm), adapted for our usage with new protocols.

## Running:
- Change the [./server/app/config.py](./server/app/config.py) file to your liking
    (don't forget to change the `SERVER_PASSWORD`).
- Change external_redis password in docker-compose.yml (of you're planning to use it).
- `docker compose up --build -d`
- **GLHF**

## Sploit descriptions and statistics

The runner can register a description when it starts:

```sh
python3 client/start_sploit.py ./my_sploit.py --server-url http://localhost:5137 \
  --server-pass YOUR_SERVER_PASSWORD --description "What this sploit attacks"
```

Descriptions are optional and limited to 1024 characters. The runner registers
the executable's basename before attacking and retries registration if the API
is temporarily unavailable. Re-registering with `--description` updates the
text; omitting it preserves an existing description. Sploits with the same
basename share one entry.

The **Sploits** tab lists registered sploits, including those with no flags,
and older sploit names already present in the flags table. All columns are
sortable. **Received** counts unique flags stored by the farm; **Accepted**
counts flags accepted by the checksystem. The 10-minute columns use the flag's
time of receipt and refresh every 30 seconds.

## Flag ingestion

The server inserts flags in SQL batches and still ignores duplicate flags.
The runner posts as soon as flags arrive and drains a backlog without a fixed
delay between successful batches. It waits 5 seconds after a transient failure;
on HTTP 413 it halves the batch and retries immediately. The bundled nginx
proxy accepts request bodies up to 4 MiB. The runner keeps exact seen-flag
deduplication for its lifetime, so this set can still grow during long,
high-volume runs.
Ingest speed is separate from checksystem submission speed, which remains
limited by `SUBMIT_FLAG_LIMIT` and `SUBMIT_PERIOD` in the server config.

Some screenshots:

![flags](resources/flags.png)

![teams](resources/teams.png)
