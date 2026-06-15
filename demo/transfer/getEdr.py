import json
import openapi_client
from openapi_client.rest import ApiException

configuration = openapi_client.Configuration(host="http://localhost:29193/management")

tp_id = input("Paste the Transfer Process ID: ").strip()

with openapi_client.ApiClient(configuration) as client:
    api = openapi_client.EDRCacheV3Api(client)
    try:
        edr = api.get_edr_entry_data_address_v3(tp_id)
        print(json.dumps(edr.model_dump(), indent=2, default=str))
    except ApiException as e:
        print(f"Error: {e.status} — {e.body}")
