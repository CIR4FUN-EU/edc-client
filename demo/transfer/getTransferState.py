import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import get_transfer_state, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

tp_id = input("Paste the Transfer Process ID: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    print("Polling for STARTED state...")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        try:
            tp = get_transfer_state(client, tp_id)
            print(f"  state: {tp.state}")
            if tp.state == "STARTED":
                print("Transfer is STARTED — you can now fetch the EDR.")
                break
        except ApiException as e:
            print(f"Error: {e.status} — {e.body}")
            break
        time.sleep(POLL_INTERVAL)
    else:
        print("Timed out waiting for transfer to start.")
