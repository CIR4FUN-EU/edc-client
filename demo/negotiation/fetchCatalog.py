import json
import openapi_client
from openapi_client.rest import ApiException

configuration = openapi_client.Configuration(host="http://localhost:29193/management")

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.CatalogV3Api(client)
    body = openapi_client.CatalogRequestV3.from_dict({
        "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
        "counterPartyId": "provider",
        "counterPartyAddress": "http://localhost:19194/protocol/2025-1",
        "protocol": "dataspace-protocol-http:2025-1",
    })
    try:
        api_response = api.request_catalog_v3_with_http_info(catalog_request_v3=body)
        catalog = json.loads(api_response.raw_data)

        print(json.dumps(catalog, indent=2))

        dataset = catalog.get("dcat:dataset") or catalog.get("dataset", {})
        if isinstance(dataset, list):
            dataset = dataset[0]
        policy = dataset.get("odrl:hasPolicy") or dataset.get("hasPolicy", {})
        if isinstance(policy, list):
            policy = policy[0]
        policy["@context"] = "http://www.w3.org/ns/odrl.jsonld"
        print(f"\nUsing offer ID: {policy.get('@id')}")

    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
