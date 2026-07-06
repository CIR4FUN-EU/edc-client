"""
End-to-end EDC flow via the Connector class, walking every step with prints.

    python full_flow.py                       # samples connectors (default)
    FLAVOR=construct_x python full_flow.py     # construct-x testbed

FLAVOR picks both the Connector preset and the env file (.env / .env.construct_x).
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

from examples.connector import example_connector, load_env

FLAVOR = load_env()

ASSET_ID        = "asset-1"
POLICY_ID       = "policy-1"
CONTRACT_DEF_ID = "contract-def-1"

provider = example_connector("PROVIDER")
consumer = example_connector("CONSUMER")

print(f"Flavor: {FLAVOR}")

# 0. provider setup (idempotent-ish: re-running fails with 409, that's fine)
print("\n[0] Provider setup...")
try:
    provider.create_asset(ASSET_ID, "https://jsonplaceholder.typicode.com/users")
    provider.create_policy(POLICY_ID)
    provider.create_contract_definition(CONTRACT_DEF_ID, POLICY_ID, POLICY_ID)
    print("    asset + policy + contract-definition created")
except Exception as e:
    print(f"    setup skipped/partial ({e}) — assuming already created")

# 1. fetch catalog
print("\n[1] Fetching catalog...")
catalog = consumer.fetch_catalog(provider)
datasets = catalog.get("dcat:dataset") or catalog.get("dataset", [])
if isinstance(datasets, dict):
    datasets = [datasets]
dataset = next(d for d in datasets if d.get("@id") == ASSET_ID)
policies = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", [])
if isinstance(policies, dict):
    policies = [policies]
offer_id = policies[0]["@id"]
print(f"    offer ID: {offer_id}")

# 2. negotiate
print("\n[2] Initiating negotiation...")
neg_id = json.loads(consumer.negotiate(provider, offer_id, ASSET_ID).data)["@id"]
print(f"    negotiation ID: {neg_id}")

# 3. poll negotiation
print("\n[3] Waiting for negotiation to finalize...")
while True:
    neg = consumer.get_negotiation(neg_id)
    print(f"    state: {neg.state}")
    if neg.state == "FINALIZED":
        agreement_id = neg.contract_agreement_id
        print(f"    agreement ID: {agreement_id}")
        break
    time.sleep(2)

# 4. start transfer
print("\n[4] Starting transfer (PULL)...")
tp_id = consumer.start_pull(provider, agreement_id)["@id"]
print(f"    transfer process ID: {tp_id}")

# 5. poll transfer + pull data
print("\n[5] Waiting for transfer to start...")
while True:
    state = consumer.get_transfer_state(tp_id).state
    print(f"    state: {state}")
    if state == "STARTED":
        endpoint, authorization = consumer.edr_endpoint_auth(consumer.get_edr(tp_id))
        resp = consumer.pull_data(endpoint, authorization)
        print("\n--- Data ---")
        print(json.dumps(resp.json(), indent=2))
        break
    time.sleep(2)
