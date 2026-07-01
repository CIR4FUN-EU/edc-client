import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from examples.connector import example_connector, load_env, ApiException

load_env()

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

consumer = example_connector("CONSUMER")
provider = example_connector("PROVIDER")

offer_id = input("Paste the offer ID (odrl:hasPolicy @id from catalog): ").strip()
asset_id = input("Enter the Asset ID: ").strip()

try:
    raw = consumer.negotiate(provider, offer_id, asset_id)
    neg_id = json.loads(raw.data)["@id"]
    print(f"Negotiation started: {neg_id}")
except ApiException as e:
    print(f"Error: {e.status} — {e.body}")
    exit(1)

print("Polling for FINALIZED state...")
deadline = time.time() + POLL_TIMEOUT
while time.time() < deadline:
    negotiation = consumer.get_negotiation(neg_id)
    print(f"  state: {negotiation.state}")
    if negotiation.state == "FINALIZED":
        print(f"\nContract Agreement ID: {negotiation.contract_agreement_id}")
        break
    time.sleep(POLL_INTERVAL)
else:
    print("Timed out waiting for negotiation to finalize.")
