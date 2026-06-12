# edc_client.TransferProcessV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer_process_state_v4**](TransferProcessV4Api.md#get_transfer_process_state_v4) | **GET** /v4/transferprocesses/{id}/state | 
[**get_transfer_process_v4**](TransferProcessV4Api.md#get_transfer_process_v4) | **GET** /v4/transferprocesses/{id} | 
[**initiate_transfer_process_v4**](TransferProcessV4Api.md#initiate_transfer_process_v4) | **POST** /v4/transferprocesses | 
[**query_transfer_processes_v4**](TransferProcessV4Api.md#query_transfer_processes_v4) | **POST** /v4/transferprocesses/request | 
[**resume_transfer_process_v4**](TransferProcessV4Api.md#resume_transfer_process_v4) | **POST** /v4/transferprocesses/{id}/resume | 
[**suspend_transfer_process_v4**](TransferProcessV4Api.md#suspend_transfer_process_v4) | **POST** /v4/transferprocesses/{id}/suspend | 
[**terminate_transfer_process_v4**](TransferProcessV4Api.md#terminate_transfer_process_v4) | **POST** /v4/transferprocesses/{id}/terminate | 


# **get_transfer_process_state_v4**
> TransferState get_transfer_process_state_v4(id)

Gets the state of a transfer process with the given ID

### Example


```python
import edc_client
from edc_client.models.transfer_state import TransferState
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_state_v4(id)
        print("The response of TransferProcessV4Api->get_transfer_process_state_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->get_transfer_process_state_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferState**](TransferState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The  transfer process&#39;s state |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An  transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_process_v4**
> TransferProcessSchema get_transfer_process_v4(id)

Gets an transfer process with the given ID

### Example


```python
import edc_client
from edc_client.models.transfer_process_schema import TransferProcessSchema
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_v4(id)
        print("The response of TransferProcessV4Api->get_transfer_process_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->get_transfer_process_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferProcessSchema**](TransferProcessSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer process |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_transfer_process_v4**
> IdResponseSchema initiate_transfer_process_v4(transfer_request_schema=transfer_request_schema)

Initiates a data transfer with the given parameters. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import edc_client
from edc_client.models.id_response_schema import IdResponseSchema
from edc_client.models.transfer_request_schema import TransferRequestSchema
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    transfer_request_schema = edc_client.TransferRequestSchema() # TransferRequestSchema |  (optional)

    try:
        api_response = api_instance.initiate_transfer_process_v4(transfer_request_schema=transfer_request_schema)
        print("The response of TransferProcessV4Api->initiate_transfer_process_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->initiate_transfer_process_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_request_schema** | [**TransferRequestSchema**](TransferRequestSchema.md)|  | [optional] 

### Return type

[**IdResponseSchema**](IdResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer was successfully initiated. Returns the transfer process ID and created timestamp |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_transfer_processes_v4**
> List[TransferProcessSchema] query_transfer_processes_v4(query_spec_schema=query_spec_schema)

Returns all transfer process according to a query

### Example


```python
import edc_client
from edc_client.models.query_spec_schema import QuerySpecSchema
from edc_client.models.transfer_process_schema import TransferProcessSchema
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    query_spec_schema = edc_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_transfer_processes_v4(query_spec_schema=query_spec_schema)
        print("The response of TransferProcessV4Api->query_transfer_processes_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->query_transfer_processes_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[TransferProcessSchema]**](TransferProcessSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer processes matching the query |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_transfer_process_v4**
> resume_transfer_process_v4(id)

Requests the resumption of a suspended transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.resume_transfer_process_v4(id)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->resume_transfer_process_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** | Request to resume the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_transfer_process_v4**
> suspend_transfer_process_v4(id, transfer_suspend_schema=transfer_suspend_schema)

Requests the suspension of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import edc_client
from edc_client.models.transfer_suspend_schema import TransferSuspendSchema
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    id = 'id_example' # str | 
    transfer_suspend_schema = edc_client.TransferSuspendSchema() # TransferSuspendSchema |  (optional)

    try:
        api_instance.suspend_transfer_process_v4(id, transfer_suspend_schema=transfer_suspend_schema)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->suspend_transfer_process_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transfer_suspend_schema** | [**TransferSuspendSchema**](TransferSuspendSchema.md)|  | [optional] 

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
**204** | Request to suspend the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |
**409** | Could not suspend the transfer process, because it is already completed or terminated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_transfer_process_v4**
> terminate_transfer_process_v4(id, transfer_terminate_schema=transfer_terminate_schema)

Requests the termination of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import edc_client
from edc_client.models.transfer_terminate_schema import TransferTerminateSchema
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
    api_instance = edc_client.TransferProcessV4Api(api_client)
    id = 'id_example' # str | 
    transfer_terminate_schema = edc_client.TransferTerminateSchema() # TransferTerminateSchema |  (optional)

    try:
        api_instance.terminate_transfer_process_v4(id, transfer_terminate_schema=transfer_terminate_schema)
    except Exception as e:
        print("Exception when calling TransferProcessV4Api->terminate_transfer_process_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transfer_terminate_schema** | [**TransferTerminateSchema**](TransferTerminateSchema.md)|  | [optional] 

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
**204** | Request to terminate the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |
**409** | Could not terminate transfer process, because it is already completed or terminated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

