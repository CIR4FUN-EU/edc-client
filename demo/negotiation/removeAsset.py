import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import remove_asset, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

PROVIDER_MANAGEMENT = os.environ["PROVIDER_MANAGEMENT"]

asset_id = input("Enter an Asset ID to remove: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=PROVIDER_MANAGEMENT)) as client:
    try:
        remove_asset(client, asset_id)
        print(f"Removed asset: {asset_id}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
