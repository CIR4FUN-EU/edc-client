"""
End-to-end EDC negotiation and transfer demo.

Usage:
  python run_demo.py               # PULL transfer (default)
  python run_demo.py --mode push   # PUSH transfer
  python run_demo.py --skip-setup  # skip provider asset/policy/contract creation
"""

import argparse
import json
import os
import time

import httpx
import openapi_client
from dotenv import load_dotenv
from openapi_client.rest import ApiException

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# --- Connector config (from .env) ---
PROVIDER_MANAGEMENT   = os.environ["PROVIDER_MANAGEMENT"]
PROVIDER_PROTOCOL     = os.environ["PROVIDER_PROTOCOL"]
PROVIDER_ID           = os.environ["PROVIDER_ID"]
CONSUMER_MANAGEMENT   = os.environ["CONSUMER_MANAGEMENT"]
CONSUMER_ID           = os.environ["CONSUMER_ID"]
PUSH_DESTINATION_URL  = os.getenv("PUSH_DESTINATION_URL", "http://localhost:4000")

# --- Hardcoded IDs ---
ASSET_ID        = "asset-1"
POLICY_ID       = "policy-1"
CONTRACT_DEF_ID = "contract-def-1"

# --- Polling config ---
POLL_INTERVAL = 2
POLL_TIMEOUT  = 12


def step(label: str) -> None:
    print(f"\n{'='*60}\n  {label}\n{'='*60}")


def setup_provider() -> None:
    cfg = openapi_client.Configuration(host=PROVIDER_MANAGEMENT)
    with openapi_client.ApiClient(cfg) as client:

        step("1/3  Create Asset")
        asset_api = openapi_client.AssetV3Api(client)
        body = openapi_client.AssetInputV3.from_dict({
            "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
            "@id": ASSET_ID,
            "properties": {
                "name": "product description",
                "contenttype": "application/json",
            },
            "dataAddress": {
                "type": "HttpData",
                "name": "Test asset",
                "baseUrl": "https://jsonplaceholder.typicode.com/users",
                "proxyPath": "true",
            },
        })
        try:
            raw = asset_api.create_asset_v3_without_preload_content(asset_input_v3=body)
            created_id = json.loads(raw.data).get("@id", ASSET_ID)
            print(f"Asset created: {created_id}")
        except ApiException as e:
            print(f"Asset error: {e.status} — {e.body}")
            raise

        step("2/3  Create Policy")
        policy_api = openapi_client.PolicyDefinitionV3Api(client)
        body = openapi_client.PolicyDefinitionInputV3.from_dict({
            "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
            "@id": POLICY_ID,
            "policy": {
                "@context": "http://www.w3.org/ns/odrl.jsonld",
                "@type": "Set",
                "permission": [],
                "prohibition": [],
                "obligation": [],
            },
        })
        try:
            raw = policy_api.create_policy_definition_v3_without_preload_content(policy_definition_input_v3=body)
            created_id = json.loads(raw.data).get("@id", POLICY_ID)
            print(f"Policy created: {created_id}")
        except ApiException as e:
            print(f"Policy error: {e.status} — {e.body}")
            raise

        step("3/3  Create Contract Definition")
        cd_api = openapi_client.ContractDefinitionV3Api(client)
        body = openapi_client.ContractDefinitionInputV3.from_dict({
            "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
            "@id": CONTRACT_DEF_ID,
            "accessPolicyId": POLICY_ID,
            "contractPolicyId": POLICY_ID,
            "assetsSelector": [],
        })
        try:
            raw = cd_api.create_contract_definition_v3_without_preload_content(contract_definition_input_v3=body)
            created_id = json.loads(raw.data).get("@id", CONTRACT_DEF_ID)
            print(f"Contract definition created: {created_id}")
        except ApiException as e:
            print(f"Contract definition error: {e.status} — {e.body}")
            raise


def fetch_catalog_offer() -> str:
    step("Fetch Catalog")
    cfg = openapi_client.Configuration(host=CONSUMER_MANAGEMENT)
    with openapi_client.ApiClient(cfg) as client:
        api = openapi_client.CatalogV3Api(client)
        body = openapi_client.CatalogRequestV3.from_dict({
            "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
            "counterPartyId": PROVIDER_ID,
            "counterPartyAddress": PROVIDER_PROTOCOL,
            "protocol": "dataspace-protocol-http:2025-1",
        })
        api_response = api.request_catalog_v3_with_http_info(catalog_request_v3=body)
        catalog = json.loads(api_response.raw_data)

        dataset = catalog.get("dcat:dataset") or catalog.get("dataset", {})
        if isinstance(dataset, list):
            dataset = dataset[0]
        policy = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", {})
        if isinstance(policy, list):
            policy = policy[0]

        offer_id = policy["@id"]
        print(f"Offer ID: {offer_id}")
        return offer_id


def negotiate(offer_id: str) -> str:
    step("Negotiate Contract")
    cfg = openapi_client.Configuration(host=CONSUMER_MANAGEMENT)
    with openapi_client.ApiClient(cfg) as client:
        api = openapi_client.ContractNegotiationV3Api(client)
        body = openapi_client.ContractRequestV3.from_dict({
            "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
            "@type": "ContractRequest",
            "counterPartyId": PROVIDER_ID,
            "counterPartyAddress": PROVIDER_PROTOCOL,
            "protocol": "dataspace-protocol-http:2025-1",
            "policy": {
                "@context": "http://www.w3.org/ns/odrl.jsonld",
                "@id": offer_id,
                "@type": "http://www.w3.org/ns/odrl/2/Offer",
                "assigner": {"@id": PROVIDER_ID},
                "target": {"@id": ASSET_ID},
            },
        })
        resp = api.initiate_contract_negotiation_v3(contract_request_v3=body)
        neg_id = resp.id
        print(f"Negotiation ID: {neg_id}")

        print("Polling for FINALIZED...")
        deadline = time.time() + POLL_TIMEOUT
        while time.time() < deadline:
            neg = api.get_negotiation_v3(neg_id)
            print(f"  state: {neg.state}")
            if neg.state == "FINALIZED":
                print(f"Agreement ID: {neg.contract_agreement_id}")
                return neg.contract_agreement_id
            time.sleep(POLL_INTERVAL)

        raise TimeoutError("Timed out waiting for negotiation to finalize.")


def start_transfer(agreement_id: str, mode: str) -> str:
    step(f"Start Transfer ({mode.upper()})")
    cfg = openapi_client.Configuration(host=CONSUMER_MANAGEMENT)

    transfer_body: dict = {
        "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
        "@type": "TransferRequestDto",
        "connectorId": PROVIDER_ID,
        "counterPartyAddress": PROVIDER_PROTOCOL,
        "contractId": agreement_id,
        "protocol": "dataspace-protocol-http:2025-1",
        "transferType": f"HttpData-{mode.upper()}",
    }
    if mode == "push":
        transfer_body["dataDestination"] = {
            "type": "HttpData",
            "baseUrl": PUSH_DESTINATION_URL,
        }

    with openapi_client.ApiClient(cfg) as client:
        api = openapi_client.TransferProcessV3Api(client)
        resp = api.initiate_transfer_process_v3(
            transfer_request_v3=openapi_client.TransferRequestV3.from_dict(transfer_body)
        )
        tp_id = resp.id
        print(f"Transfer Process ID: {tp_id}")

        print("Polling for STARTED...")
        deadline = time.time() + POLL_TIMEOUT
        while time.time() < deadline:
            tp = api.get_transfer_process_v3(tp_id)
            print(f"  state: {tp.state}")
            if tp.state == "STARTED":
                print("Transfer STARTED.")
                return tp_id
            time.sleep(POLL_INTERVAL)

        raise TimeoutError("Timed out waiting for transfer to start.")


def pull_data(tp_id: str) -> None:
    step("Fetch EDR + Pull Data")
    cfg = openapi_client.Configuration(host=CONSUMER_MANAGEMENT)
    with openapi_client.ApiClient(cfg) as client:
        edr_api = openapi_client.EDRCacheV3Api(client)
        edr = edr_api.get_edr_entry_data_address_v3(tp_id)

    edr_dict = edr.model_dump()
    print("EDR:", json.dumps(edr_dict, indent=2, default=str))

    endpoint      = edr_dict.get("endpoint") or edr_dict.get("additional_properties", {}).get("endpoint")
    authorization = edr_dict.get("authorization") or edr_dict.get("additional_properties", {}).get("authorization")

    if not endpoint or not authorization:
        print("Could not extract endpoint/authorization from EDR. Raw EDR printed above.")
        return

    print(f"\nGET {endpoint}")
    response = httpx.get(endpoint, headers={"Authorization": authorization})
    response.raise_for_status()
    print(json.dumps(response.json(), indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="EDC end-to-end demo")
    parser.add_argument(
        "--mode",
        choices=["pull", "push"],
        default="pull",
        help="Transfer type (default: pull)",
    )
    parser.add_argument(
        "--skip-setup",
        action="store_true",
        help="Skip provider asset/policy/contract definition creation",
    )
    args = parser.parse_args()

    print(f"Provider : {PROVIDER_MANAGEMENT}")
    print(f"Consumer : {CONSUMER_MANAGEMENT}")
    print(f"Mode     : {args.mode.upper()}")
    print(f"Setup    : {'skipped' if args.skip_setup else 'enabled'}")

    if not args.skip_setup:
        setup_provider()

    offer_id     = fetch_catalog_offer()
    agreement_id = negotiate(offer_id)
    tp_id        = start_transfer(agreement_id, args.mode)

    if args.mode == "pull":
        pull_data(tp_id)
    else:
        step("Done")
        print(f"PUSH transfer started. Provider will push data to: {PUSH_DESTINATION_URL}")


if __name__ == "__main__":
    main()
