# openapi_client.DataplaneSignalingRegistrationV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5**](DataplaneSignalingRegistrationV5betaApi.md#delete_v5) | **DELETE** /v5beta/participants/{participantContextId}/dataplanes/{dataplaneId} | 
[**register_v5**](DataplaneSignalingRegistrationV5betaApi.md#register_v5) | **PUT** /v5beta/participants/{participantContextId}/dataplanes | 


# **delete_v5**
> delete_v5(participant_context_id, dataplane_id)

Delete a Dataplane instance

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DataplaneSignalingRegistrationV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    dataplane_id = 'dataplane_id_example' # str | 

    try:
        api_instance.delete_v5(participant_context_id, dataplane_id)
    except Exception as e:
        print("Exception when calling DataplaneSignalingRegistrationV5betaApi->delete_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **dataplane_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataplane instance correctly deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_v5**
> register_v5(participant_context_id, data_plane_registration_message=data_plane_registration_message)

Register or update a Dataplane instance

### Example


```python
import openapi_client
from openapi_client.models.data_plane_registration_message import DataPlaneRegistrationMessage
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
    api_instance = openapi_client.DataplaneSignalingRegistrationV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    data_plane_registration_message = openapi_client.DataPlaneRegistrationMessage() # DataPlaneRegistrationMessage |  (optional)

    try:
        api_instance.register_v5(participant_context_id, data_plane_registration_message=data_plane_registration_message)
    except Exception as e:
        print("Exception when calling DataplaneSignalingRegistrationV5betaApi->register_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **data_plane_registration_message** | [**DataPlaneRegistrationMessage**](DataPlaneRegistrationMessage.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataplane instance correctly registered |  -  |
**400** | Request was malformed |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

