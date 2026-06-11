# openapi_client.TransferProcessV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer_process_state_v5**](TransferProcessV5betaApi.md#get_transfer_process_state_v5) | **GET** /v5beta/participants/{participantContextId}/transferprocesses/{id}/state | 
[**get_transfer_process_v5**](TransferProcessV5betaApi.md#get_transfer_process_v5) | **GET** /v5beta/participants/{participantContextId}/transferprocesses/{id} | 
[**initiate_transfer_process_v5**](TransferProcessV5betaApi.md#initiate_transfer_process_v5) | **POST** /v5beta/participants/{participantContextId}/transferprocesses | 
[**query_transfer_processes_v5**](TransferProcessV5betaApi.md#query_transfer_processes_v5) | **POST** /v5beta/participants/{participantContextId}/transferprocesses/request | 
[**resume_transfer_process_v5**](TransferProcessV5betaApi.md#resume_transfer_process_v5) | **POST** /v5beta/participants/{participantContextId}/transferprocesses/{id}/resume | 
[**suspend_transfer_process_v5**](TransferProcessV5betaApi.md#suspend_transfer_process_v5) | **POST** /v5beta/participants/{participantContextId}/transferprocesses/{id}/suspend | 
[**terminate_transfer_process_v5**](TransferProcessV5betaApi.md#terminate_transfer_process_v5) | **POST** /v5beta/participants/{participantContextId}/transferprocesses/{id}/terminate | 


# **get_transfer_process_state_v5**
> TransferState get_transfer_process_state_v5(participant_context_id, id)

Gets the state of a transfer process with the given ID

### Example


```python
import openapi_client
from openapi_client.models.transfer_state import TransferState
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_state_v5(participant_context_id, id)
        print("The response of TransferProcessV5betaApi->get_transfer_process_state_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->get_transfer_process_state_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **get_transfer_process_v5**
> TransferProcessSchema get_transfer_process_v5(participant_context_id, id)

Gets an transfer process with the given ID

### Example


```python
import openapi_client
from openapi_client.models.transfer_process_schema import TransferProcessSchema
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_v5(participant_context_id, id)
        print("The response of TransferProcessV5betaApi->get_transfer_process_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->get_transfer_process_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **initiate_transfer_process_v5**
> IdResponseSchema initiate_transfer_process_v5(participant_context_id, transfer_request_schema=transfer_request_schema)

Initiates a data transfer with the given parameters. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.id_response_schema import IdResponseSchema
from openapi_client.models.transfer_request_schema import TransferRequestSchema
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    transfer_request_schema = openapi_client.TransferRequestSchema() # TransferRequestSchema |  (optional)

    try:
        api_response = api_instance.initiate_transfer_process_v5(participant_context_id, transfer_request_schema=transfer_request_schema)
        print("The response of TransferProcessV5betaApi->initiate_transfer_process_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->initiate_transfer_process_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **query_transfer_processes_v5**
> List[TransferProcessSchema] query_transfer_processes_v5(participant_context_id, query_spec_schema=query_spec_schema)

Returns all transfer process according to a query

### Example


```python
import openapi_client
from openapi_client.models.query_spec_schema import QuerySpecSchema
from openapi_client.models.transfer_process_schema import TransferProcessSchema
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_transfer_processes_v5(participant_context_id, query_spec_schema=query_spec_schema)
        print("The response of TransferProcessV5betaApi->query_transfer_processes_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->query_transfer_processes_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **resume_transfer_process_v5**
> resume_transfer_process_v5(participant_context_id, id)

Requests the resumption of a suspended transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_instance.resume_transfer_process_v5(participant_context_id, id)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->resume_transfer_process_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **suspend_transfer_process_v5**
> suspend_transfer_process_v5(participant_context_id, id, transfer_suspend_schema=transfer_suspend_schema)

Requests the suspension of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.transfer_suspend_schema import TransferSuspendSchema
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 
    transfer_suspend_schema = openapi_client.TransferSuspendSchema() # TransferSuspendSchema |  (optional)

    try:
        api_instance.suspend_transfer_process_v5(participant_context_id, id, transfer_suspend_schema=transfer_suspend_schema)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->suspend_transfer_process_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **terminate_transfer_process_v5**
> terminate_transfer_process_v5(participant_context_id, id, transfer_terminate_schema=transfer_terminate_schema)

Requests the termination of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.transfer_terminate_schema import TransferTerminateSchema
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
    api_instance = openapi_client.TransferProcessV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 
    transfer_terminate_schema = openapi_client.TransferTerminateSchema() # TransferTerminateSchema |  (optional)

    try:
        api_instance.terminate_transfer_process_v5(participant_context_id, id, transfer_terminate_schema=transfer_terminate_schema)
    except Exception as e:
        print("Exception when calling TransferProcessV5betaApi->terminate_transfer_process_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

