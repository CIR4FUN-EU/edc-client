import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import start_pull, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]
PROVIDER_PROTOCOL   = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID         = os.environ["PROVIDER_ID"]

agreement_id = input("Paste the Contract Agreement ID: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    try:
        tp = start_pull(client, PROVIDER_ID, PROVIDER_PROTOCOL, agreement_id)
        print(f"Transfer Process ID: {tp['@id']}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
