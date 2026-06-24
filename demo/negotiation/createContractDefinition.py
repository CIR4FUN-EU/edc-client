import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import create_contract_definition, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

PROVIDER_MANAGEMENT = os.environ["PROVIDER_MANAGEMENT"]

cd_id     = input("Enter a Contract Definition ID: ").strip()
policy_id = input("Enter the Policy ID to use: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=PROVIDER_MANAGEMENT)) as client:
    try:
        response = create_contract_definition(client, cd_id, policy_id, policy_id)
        print(json.dumps(response, indent=2))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
