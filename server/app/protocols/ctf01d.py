import requests
import logging

from models import FlagStatus, SubmitResult

logger = logging.getLogger(__name__)

TIMEOUT = 5

def submit_flags(flags, config):
    for flag in flags:
        r = requests.get(f"{config['SYSTEM_URL']}?teamid={config['TEAM_ID']}&flag={flag.flag}", 
                         timeout=TIMEOUT)

        if r.status_code == 200:
            found_status = FlagStatus.ACCEPTED
        else:
            found_status = FlagStatus.REJECTED
         
        yield SubmitResult(flag.flag, found_status, r.text)
