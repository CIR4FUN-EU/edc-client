# openapi_client.DiscoveryV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discover_v5**](DiscoveryV5betaApi.md#discover_v5) | **POST** /v5beta/participants/{participantContextId}/discover/request | 


# **discover_v5**
> List[DiscoveryResponseSchema] discover_v5(participant_context_id, discovery_request_schema=discovery_request_schema)

Discovers the dataspace profiles usable to communicate with a counter party. Resolves the counter party's `.well-known/dspace-version` endpoint (either directly via `counterPartyAddress` or by resolving the `DataService` entry of the DID document for `counterPartyId`) and returns the intersection with the profiles associated to the participant context.

### Example


```python
import openapi_client
from openapi_client.models.discovery_request_schema import DiscoveryRequestSchema
from openapi_client.models.discovery_response_schema import DiscoveryResponseSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DiscoveryV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    discovery_request_schema = openapi_client.DiscoveryRequestSchema() # DiscoveryRequestSchema |  (optional)

    try:
        api_response = api_instance.discover_v5(participant_context_id, discovery_request_schema=discovery_request_schema)
        print("The response of DiscoveryV5betaApi->discover_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryV5betaApi->discover_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **discovery_request_schema** | [**DiscoveryRequestSchema**](DiscoveryRequestSchema.md)|  | [optional] 

### Return type

[**List[DiscoveryResponseSchema]**](DiscoveryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profiles that match the counter party. |  -  |
**400** | Request body was malformed, the counter party could not be reached, or no DID service endpoint was found. |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

