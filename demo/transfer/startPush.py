import json
import openapi_client
from openapi_client.rest import ApiException

configuration = openapi_client.Configuration(host="http://localhost:29193/management")

agreement_id = input("Paste the Contract Agreement ID: ").strip()

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.TransferProcessV3Api(client)
    body = openapi_client.TransferRequestV3.from_dict({
        "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
        "@type": "TransferRequestDto",
        "connectorId": "connector-1",
        "counterPartyAddress": "http://localhost:19194/protocol/2025-1",
        "contractId": agreement_id,
        "protocol": "dataspace-protocol-http:2025-1",
        "transferType": "HttpData-PUSH",
        "dataDestination": {
            "type": "HttpData",
            "baseUrl": "http://localhost:4000",  # your receiving server
        },
    })
    try:
        resp = api.initiate_transfer_process_v3(transfer_request_v3=body)
        print(f"Transfer Process ID: {resp.id}")
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
