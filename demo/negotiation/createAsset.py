import json
import openapi_client
from openapi_client.rest import ApiException

configuration = openapi_client.Configuration(host="http://localhost:19193/management")

asset_id = input("Enter an Asset ID: ").strip()

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.AssetV3Api(client)
    body = openapi_client.AssetInputV3.from_dict({
        "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
        "@id": asset_id,
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
        raw = api.create_asset_v3_without_preload_content(asset_input_v3=body)
        print(json.dumps(json.loads(raw.data), indent=2))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
