import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(host="http://localhost:19193/management")

asset_id = input("Enter an Asset ID to remove: ").strip()


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetV3Api(api_client)
    id = asset_id # str | 

    try:
        api_instance.remove_asset_v3(id)
    except Exception as e:
        print("Exception when calling AssetV3Api->remove_asset_v3: %s\n" % e)
    