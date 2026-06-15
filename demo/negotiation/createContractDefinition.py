import json
import openapi_client
from openapi_client.rest import ApiException

configuration = openapi_client.Configuration(host="http://localhost:19193/management")

cd_id     = input("Enter a Contract Definition ID: ").strip()
policy_id = input("Enter the Policy ID to use: ").strip()

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.ContractDefinitionV3Api(client)
    body = openapi_client.ContractDefinitionInputV3.from_dict({
        "@context": {"@vocab": "https://w3id.org/edc/v0.0.1/ns/"},
        "@id": cd_id,
        "accessPolicyId": policy_id,
        "contractPolicyId": policy_id,
        "assetsSelector": [],
    })
    try:
        raw = api.create_contract_definition_v3_without_preload_content(contract_definition_input_v3=body)
        print(json.dumps(json.loads(raw.data), indent=2))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
