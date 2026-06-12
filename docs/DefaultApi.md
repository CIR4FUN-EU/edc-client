# edc_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deprovision**](DefaultApi.md#deprovision) | **POST** /{flowId}/{resourceId}/deprovision | 
[**provision**](DefaultApi.md#provision) | **POST** /{flowId}/{resourceId}/provision | 


# **deprovision**
> deprovision(flow_id, resource_id)

### Example


```python
import edc_client
from edc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = edc_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with edc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edc_client.DefaultApi(api_client)
    flow_id = 'flow_id_example' # str | 
    resource_id = 'resource_id_example' # str | 

    try:
        api_instance.deprovision(flow_id, resource_id)
    except Exception as e:
        print("Exception when calling DefaultApi->deprovision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **resource_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision**
> provision(flow_id, resource_id, provision_http_response=provision_http_response)

### Example


```python
import edc_client
from edc_client.models.provision_http_response import ProvisionHttpResponse
from edc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = edc_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with edc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edc_client.DefaultApi(api_client)
    flow_id = 'flow_id_example' # str | 
    resource_id = 'resource_id_example' # str | 
    provision_http_response = edc_client.ProvisionHttpResponse() # ProvisionHttpResponse |  (optional)

    try:
        api_instance.provision(flow_id, resource_id, provision_http_response=provision_http_response)
    except Exception as e:
        print("Exception when calling DefaultApi->provision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **resource_id** | **str**|  | 
 **provision_http_response** | [**ProvisionHttpResponse**](ProvisionHttpResponse.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

