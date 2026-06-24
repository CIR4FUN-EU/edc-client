import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import fetch_catalog, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]
PROVIDER_PROTOCOL   = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID         = os.environ["PROVIDER_ID"]

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    try:
        catalog = fetch_catalog(client, PROVIDER_ID, PROVIDER_PROTOCOL)
        print(json.dumps(catalog, indent=2))

        dataset = catalog.get("dcat:dataset") or catalog.get("dataset", {})
        if isinstance(dataset, list):
            dataset = dataset[0]
        policy = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", {})
        if isinstance(policy, list):
            policy = policy[0]
        print(f"\nUsing offer ID: {policy.get('@id')}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
