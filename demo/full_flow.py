"""
End-to-end EDC flow against the samples connector (demo/connector-configs/).
Imports the helpers from demo_functions.py and walks every step with prints.

    python full_flow.py

No auth: the samples connector exposes the management API without an api key.
Config comes from demo/.env (PROVIDER_*/CONSUMER_*).
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

import edc_client
from dotenv import load_dotenv
from demo_functions import (
    create_asset,
    create_policy,
    create_contract_definition,
    fetch_catalog,
    negotiate,
    start_pull,
    get_edr,
    get_transfer_state,
    pull_data,
    _edr_endpoint_auth,
)

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

PROVIDER_MANAGEMENT = os.environ["PROVIDER_MANAGEMENT"]
PROVIDER_PROTOCOL   = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID         = os.environ["PROVIDER_ID"]
CONSUMER_MANAGEMENT = os.environ["CONSUMER_MANAGEMENT"]

ASSET_ID        = "asset-1"
POLICY_ID       = "policy-1"
CONTRACT_DEF_ID = "contract-def-1"

provider = edc_client.ApiClient(edc_client.Configuration(host=PROVIDER_MANAGEMENT))
consumer = edc_client.ApiClient(edc_client.Configuration(host=CONSUMER_MANAGEMENT))


# 0. provider setup (idempotent-ish: re-running fails with 409, that's fine)
print("\n[0] Provider setup...")
try:
    create_asset(provider, ASSET_ID, "https://jsonplaceholder.typicode.com/users")
    create_policy(provider, POLICY_ID)
    create_contract_definition(provider, CONTRACT_DEF_ID, POLICY_ID, POLICY_ID)
    print("    asset + policy + contract-definition created")
except Exception as e:
    print(f"    setup skipped/partial ({e}) — assuming already created")

# 1. fetch catalog
print("\n[1] Fetching catalog...")
catalog = fetch_catalog(consumer, PROVIDER_ID, PROVIDER_PROTOCOL)
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
raw = negotiate(consumer, PROVIDER_ID, PROVIDER_PROTOCOL, offer_id, ASSET_ID)
neg_id = json.loads(raw.data)["@id"]
print(f"    negotiation ID: {neg_id}")

# 3. poll negotiation
print("\n[3] Waiting for negotiation to finalize...")
neg_api = edc_client.ContractNegotiationV3Api(consumer)
while True:
    neg = neg_api.get_negotiation_v3(neg_id)
    print(f"    state: {neg.state}")
    if neg.state == "FINALIZED":
        agreement_id = neg.contract_agreement_id
        print(f"    agreement ID: {agreement_id}")
        break
    time.sleep(2)

# 4. start transfer
print("\n[4] Starting transfer (PULL)...")
tp_id = start_pull(consumer, PROVIDER_ID, PROVIDER_PROTOCOL, agreement_id)["@id"]
print(f"    transfer process ID: {tp_id}")

# 5. poll transfer + pull data
print("\n[5] Waiting for transfer to start...")
while True:
    state = get_transfer_state(consumer, tp_id).state
    print(f"    state: {state}")
    if state == "STARTED":
        endpoint, authorization = _edr_endpoint_auth(get_edr(consumer, tp_id))
        resp = pull_data(endpoint, authorization)
        print("\n--- Data ---")
        print(json.dumps(resp.json(), indent=2))
        break
    time.sleep(2)
