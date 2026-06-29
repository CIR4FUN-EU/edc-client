import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import list_assets, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

PROVIDER_MANAGEMENT = os.environ["PROVIDER_MANAGEMENT"]
BASE_URL = "https://jsonplaceholder.typicode.com/users"

print("Assets: \n")

with edc_client.ApiClient(edc_client.Configuration(host=PROVIDER_MANAGEMENT)) as client:
    try:
        response = list_assets(client)
        print(json.dumps(response, indent=2))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
