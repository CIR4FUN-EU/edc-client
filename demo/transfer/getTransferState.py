import time
import openapi_client
from openapi_client.rest import ApiException

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

configuration = openapi_client.Configuration(host="http://localhost:29193/management")

tp_id = input("Paste the Transfer Process ID: ").strip()

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.TransferProcessV3Api(client)

    print("Polling for STARTED state...")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        try:
            tp = api.get_transfer_process_v3(tp_id)
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
