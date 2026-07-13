import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from examples.connector import example_connector, load_env, ApiException

load_env()

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

consumer = example_connector("CONSUMER")

tp_id = input("Paste the Transfer Process ID: ").strip()

print("Polling for STARTED state...")
deadline = time.time() + POLL_TIMEOUT
while time.time() < deadline:
    try:
        state = consumer.get_transfer_state(tp_id)["state"]
        print(f"  state: {state}")
        if state == "STARTED":
            print("Transfer is STARTED — you can now fetch the EDR.")
            break
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
        break
    time.sleep(POLL_INTERVAL)
else:
    print("Timed out waiting for transfer to start.")
