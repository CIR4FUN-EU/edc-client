# openapi_client.EDRCacheV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_edr_entry_data_address_v3**](EDRCacheV3Api.md#get_edr_entry_data_address_v3) | **GET** /v3/edrs/{transferProcessId}/dataaddress | 
[**remove_edr_entry_v3**](EDRCacheV3Api.md#remove_edr_entry_v3) | **DELETE** /v3/edrs/{transferProcessId} | 
[**request_edr_entries_v3**](EDRCacheV3Api.md#request_edr_entries_v3) | **POST** /v3/edrs/request | 


# **get_edr_entry_data_address_v3**
> DataAddress get_edr_entry_data_address_v3(transfer_process_id)

Gets the EDR data address with the given transfer process ID

### Example


```python
import openapi_client
from openapi_client.models.data_address import DataAddress
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
    api_instance = openapi_client.EDRCacheV3Api(api_client)
    transfer_process_id = 'transfer_process_id_example' # str | 

    try:
        api_response = api_instance.get_edr_entry_data_address_v3(transfer_process_id)
        print("The response of EDRCacheV3Api->get_edr_entry_data_address_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EDRCacheV3Api->get_edr_entry_data_address_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_process_id** | **str**|  | 

### Return type

[**DataAddress**](DataAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data address |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An EDR data address with the given transfer process ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_edr_entry_v3**
> remove_edr_entry_v3(transfer_process_id)

Removes an EDR entry given the transfer process ID

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
    api_instance = openapi_client.EDRCacheV3Api(api_client)
    transfer_process_id = 'transfer_process_id_example' # str | 

    try:
        api_instance.remove_edr_entry_v3(transfer_process_id)
    except Exception as e:
        print("Exception when calling EDRCacheV3Api->remove_edr_entry_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_process_id** | **str**|  | 

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
**204** | EDR entry was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An EDR entry with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_edr_entries_v3**
> List[EndpointDataReferenceEntryV3] request_edr_entries_v3(query_spec=query_spec)

Request all Edr entries according to a particular query

### Example


```python
import openapi_client
from openapi_client.models.endpoint_data_reference_entry_v3 import EndpointDataReferenceEntryV3
from openapi_client.models.query_spec import QuerySpec
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
    api_instance = openapi_client.EDRCacheV3Api(api_client)
    query_spec = openapi_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.request_edr_entries_v3(query_spec=query_spec)
        print("The response of EDRCacheV3Api->request_edr_entries_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EDRCacheV3Api->request_edr_entries_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[EndpointDataReferenceEntryV3]**](EndpointDataReferenceEntryV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edr entries matching the query |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

