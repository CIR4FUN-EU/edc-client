# openapi_client.TransferProcessV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deprovision_transfer_process_v3**](TransferProcessV3Api.md#deprovision_transfer_process_v3) | **POST** /v3/transferprocesses/{id}/deprovision | 
[**get_transfer_process_state_v3**](TransferProcessV3Api.md#get_transfer_process_state_v3) | **GET** /v3/transferprocesses/{id}/state | 
[**get_transfer_process_v3**](TransferProcessV3Api.md#get_transfer_process_v3) | **GET** /v3/transferprocesses/{id} | 
[**initiate_transfer_process_v3**](TransferProcessV3Api.md#initiate_transfer_process_v3) | **POST** /v3/transferprocesses | 
[**query_transfer_processes_v3**](TransferProcessV3Api.md#query_transfer_processes_v3) | **POST** /v3/transferprocesses/request | 
[**resume_transfer_process_v3**](TransferProcessV3Api.md#resume_transfer_process_v3) | **POST** /v3/transferprocesses/{id}/resume | 
[**suspend_transfer_process_v3**](TransferProcessV3Api.md#suspend_transfer_process_v3) | **POST** /v3/transferprocesses/{id}/suspend | 
[**terminate_transfer_process_v3**](TransferProcessV3Api.md#terminate_transfer_process_v3) | **POST** /v3/transferprocesses/{id}/terminate | 


# **deprovision_transfer_process_v3**
> deprovision_transfer_process_v3(id)

Requests the deprovisioning of resources associated with a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.deprovision_transfer_process_v3(id)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->deprovision_transfer_process_v3: %s\n" % e)
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
**204** | Request to deprovision the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_process_state_v3**
> TransferStateV3 get_transfer_process_state_v3(id)

Gets the state of a transfer process with the given ID

### Example


```python
import openapi_client
from openapi_client.models.transfer_state_v3 import TransferStateV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_state_v3(id)
        print("The response of TransferProcessV3Api->get_transfer_process_state_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->get_transfer_process_state_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferStateV3**](TransferStateV3.md)

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

# **get_transfer_process_v3**
> TransferProcessV3 get_transfer_process_v3(id)

Gets an transfer process with the given ID

### Example


```python
import openapi_client
from openapi_client.models.transfer_process_v3 import TransferProcessV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_v3(id)
        print("The response of TransferProcessV3Api->get_transfer_process_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->get_transfer_process_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferProcessV3**](TransferProcessV3.md)

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

# **initiate_transfer_process_v3**
> IdResponse initiate_transfer_process_v3(transfer_request_v3=transfer_request_v3)

Initiates a data transfer with the given parameters. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.id_response import IdResponse
from openapi_client.models.transfer_request_v3 import TransferRequestV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    transfer_request_v3 = openapi_client.TransferRequestV3() # TransferRequestV3 |  (optional)

    try:
        api_response = api_instance.initiate_transfer_process_v3(transfer_request_v3=transfer_request_v3)
        print("The response of TransferProcessV3Api->initiate_transfer_process_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->initiate_transfer_process_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_request_v3** | [**TransferRequestV3**](TransferRequestV3.md)|  | [optional] 

### Return type

[**IdResponse**](IdResponse.md)

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

# **query_transfer_processes_v3**
> List[TransferProcessV3] query_transfer_processes_v3(query_spec=query_spec)

Returns all transfer process according to a query

### Example


```python
import openapi_client
from openapi_client.models.query_spec import QuerySpec
from openapi_client.models.transfer_process_v3 import TransferProcessV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    query_spec = openapi_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.query_transfer_processes_v3(query_spec=query_spec)
        print("The response of TransferProcessV3Api->query_transfer_processes_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->query_transfer_processes_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[TransferProcessV3]**](TransferProcessV3.md)

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

# **resume_transfer_process_v3**
> resume_transfer_process_v3(id)

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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.resume_transfer_process_v3(id)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->resume_transfer_process_v3: %s\n" % e)
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

# **suspend_transfer_process_v3**
> suspend_transfer_process_v3(id, suspend_transfer_v3=suspend_transfer_v3)

Requests the suspension of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.suspend_transfer_v3 import SuspendTransferV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 
    suspend_transfer_v3 = openapi_client.SuspendTransferV3() # SuspendTransferV3 |  (optional)

    try:
        api_instance.suspend_transfer_process_v3(id, suspend_transfer_v3=suspend_transfer_v3)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->suspend_transfer_process_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **suspend_transfer_v3** | [**SuspendTransferV3**](SuspendTransferV3.md)|  | [optional] 

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

# **terminate_transfer_process_v3**
> terminate_transfer_process_v3(id, terminate_transfer_v3=terminate_transfer_v3)

Requests the termination of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

### Example


```python
import openapi_client
from openapi_client.models.terminate_transfer_v3 import TerminateTransferV3
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
    api_instance = openapi_client.TransferProcessV3Api(api_client)
    id = 'id_example' # str | 
    terminate_transfer_v3 = openapi_client.TerminateTransferV3() # TerminateTransferV3 |  (optional)

    try:
        api_instance.terminate_transfer_process_v3(id, terminate_transfer_v3=terminate_transfer_v3)
    except Exception as e:
        print("Exception when calling TransferProcessV3Api->terminate_transfer_process_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **terminate_transfer_v3** | [**TerminateTransferV3**](TerminateTransferV3.md)|  | [optional] 

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

