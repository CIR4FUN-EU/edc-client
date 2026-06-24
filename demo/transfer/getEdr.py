import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import get_edr, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]

tp_id = input("Paste the Transfer Process ID: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    try:
        edr = get_edr(client, tp_id)
        print(json.dumps(edr.model_dump(), indent=2, default=str))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
