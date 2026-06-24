import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import edc_client
from dotenv import load_dotenv
from demo_functions import negotiate, ApiException

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]
PROVIDER_PROTOCOL   = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID         = os.environ["PROVIDER_ID"]

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

offer_id = input("Paste the offer ID (odrl:hasPolicy @id from catalog): ").strip()
asset_id = input("Enter the Asset ID: ").strip()

with edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT)) as client:
    try:
        raw = negotiate(client, PROVIDER_ID, PROVIDER_PROTOCOL, offer_id, asset_id)
        neg_id = json.loads(raw.data)["@id"]
        print(f"Negotiation started: {neg_id}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
        exit(1)

    neg_api = edc_client.ContractNegotiationV3Api(client)
    print("Polling for FINALIZED state...")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        negotiation = neg_api.get_negotiation_v3(neg_id)
        print(f"  state: {negotiation.state}")
        if negotiation.state == "FINALIZED":
            print(f"\nContract Agreement ID: {negotiation.contract_agreement_id}")
            break
        time.sleep(POLL_INTERVAL)
    else:
        print("Timed out waiting for negotiation to finalize.")
