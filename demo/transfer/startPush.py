import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import start_push, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]
PROVIDER_PROTOCOL   = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID         = os.environ["PROVIDER_ID"]
PUSH_DESTINATION_URL = os.environ["PUSH_DESTINATION_URL"]

agreement_id = input("Paste the Contract Agreement ID: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    try:
        resp = start_push(client, PROVIDER_ID, PROVIDER_PROTOCOL, agreement_id, PUSH_DESTINATION_URL)
        print(f"Transfer Process ID: {resp.id}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
