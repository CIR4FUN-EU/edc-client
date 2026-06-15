import time
import openapi_client
from openapi_client.rest import ApiException

CONSUMER_MANAGEMENT = "http://localhost:29193/management"
PROVIDER_PROTOCOL   = "http://localhost:19194/protocol/2025-1"
PROVIDER_ID         = "connector-1"

POLL_INTERVAL = 2
POLL_TIMEOUT  = 60

offer_id = input("Paste the offer ID (odrl:hasPolicy @id from catalog): ").strip()
asset_id = input("Enter the Asset ID: ").strip()

configuration = openapi_client.Configuration(host=CONSUMER_MANAGEMENT)

with openapi_client.ApiClient(configuration) as client:
    neg_api = openapi_client.ContractNegotiationV3Api(client)

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
            "target": {"@id": asset_id},
        },
    })

    try:
        resp = neg_api.initiate_contract_negotiation_v3(contract_request_v3=body)
        neg_id = resp.id
        print(f"Negotiation started: {neg_id}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
        exit(1)

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
