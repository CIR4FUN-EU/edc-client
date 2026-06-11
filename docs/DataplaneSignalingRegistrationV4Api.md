# openapi_client.DataplaneSignalingRegistrationV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DataplaneSignalingRegistrationV4Api.md#delete) | **DELETE** /v4/dataplanes/{dataplaneId} | 


# **delete**
> delete(dataplane_id)

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
    api_instance = openapi_client.DataplaneSignalingRegistrationV4Api(api_client)
    dataplane_id = 'dataplane_id_example' # str | 

    try:
        api_instance.delete(dataplane_id)
    except Exception as e:
        print("Exception when calling DataplaneSignalingRegistrationV4Api->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

