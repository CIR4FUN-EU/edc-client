# openapi_client.ContractNegotiationV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_negotiation_v3**](ContractNegotiationV3Api.md#delete_negotiation_v3) | **DELETE** /v3/contractnegotiations/{id} | 
[**get_agreement_for_negotiation_v3**](ContractNegotiationV3Api.md#get_agreement_for_negotiation_v3) | **GET** /v3/contractnegotiations/{id}/agreement | 
[**get_negotiation_state_v3**](ContractNegotiationV3Api.md#get_negotiation_state_v3) | **GET** /v3/contractnegotiations/{id}/state | 
[**get_negotiation_v3**](ContractNegotiationV3Api.md#get_negotiation_v3) | **GET** /v3/contractnegotiations/{id} | 
[**initiate_contract_negotiation_v3**](ContractNegotiationV3Api.md#initiate_contract_negotiation_v3) | **POST** /v3/contractnegotiations | 
[**query_negotiations_v3**](ContractNegotiationV3Api.md#query_negotiations_v3) | **POST** /v3/contractnegotiations/request | 
[**terminate_negotiation_v3**](ContractNegotiationV3Api.md#terminate_negotiation_v3) | **POST** /v3/contractnegotiations/{id}/terminate | 


# **delete_negotiation_v3**
> delete_negotiation_v3(id)

Deletes the contract negotiation with the given ID. Only terminated negotiations without agreement will be deleted

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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_negotiation_v3(id)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->delete_negotiation_v3: %s\n" % e)
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
**204** | ContractNegotiation is deleted |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |
**409** | The given contract negotiation cannot be deleted due to a wrong state or has existing contract agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agreement_for_negotiation_v3**
> ContractAgreement get_agreement_for_negotiation_v3(id)

Gets a contract agreement for a contract negotiation with the given ID

### Example


```python
import openapi_client
from openapi_client.models.contract_agreement import ContractAgreement
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_for_negotiation_v3(id)
        print("The response of ContractNegotiationV3Api->get_agreement_for_negotiation_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->get_agreement_for_negotiation_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractAgreement**](ContractAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract agreement that is attached to the negotiation, or null |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiation_state_v3**
> NegotiationState get_negotiation_state_v3(id)

Gets the state of a contract negotiation with the given ID

### Example


```python
import openapi_client
from openapi_client.models.negotiation_state import NegotiationState
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_state_v3(id)
        print("The response of ContractNegotiationV3Api->get_negotiation_state_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->get_negotiation_state_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NegotiationState**](NegotiationState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiation&#39;s state |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiation_v3**
> ContractNegotiation get_negotiation_v3(id)

Gets a contract negotiation with the given ID

### Example


```python
import openapi_client
from openapi_client.models.contract_negotiation import ContractNegotiation
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_v3(id)
        print("The response of ContractNegotiationV3Api->get_negotiation_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->get_negotiation_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractNegotiation**](ContractNegotiation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiation |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_contract_negotiation_v3**
> IdResponse initiate_contract_negotiation_v3(contract_request_v3=contract_request_v3)

Initiates a contract negotiation for a given offer and with the given counter part. Please note that successfully invoking this endpoint only means that the negotiation was initiated. Clients must poll the /{id}/state endpoint to track the state

### Example


```python
import openapi_client
from openapi_client.models.contract_request_v3 import ContractRequestV3
from openapi_client.models.id_response import IdResponse
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    contract_request_v3 = openapi_client.ContractRequestV3() # ContractRequestV3 |  (optional)

    try:
        api_response = api_instance.initiate_contract_negotiation_v3(contract_request_v3=contract_request_v3)
        print("The response of ContractNegotiationV3Api->initiate_contract_negotiation_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->initiate_contract_negotiation_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_request_v3** | [**ContractRequestV3**](ContractRequestV3.md)|  | [optional] 

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
**200** | The negotiation was successfully initiated. Returns the contract negotiation ID and created timestamp |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_negotiations_v3**
> List[ContractNegotiation] query_negotiations_v3(query_spec=query_spec)

Returns all contract negotiations according to a query

### Example


```python
import openapi_client
from openapi_client.models.contract_negotiation import ContractNegotiation
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    query_spec = openapi_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.query_negotiations_v3(query_spec=query_spec)
        print("The response of ContractNegotiationV3Api->query_negotiations_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->query_negotiations_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[ContractNegotiation]**](ContractNegotiation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiations that match the query |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_negotiation_v3**
> terminate_negotiation_v3(id, terminate_negotiation_v3=terminate_negotiation_v3)

Terminates the contract negotiation.

### Example


```python
import openapi_client
from openapi_client.models.terminate_negotiation_v3 import TerminateNegotiationV3
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
    api_instance = openapi_client.ContractNegotiationV3Api(api_client)
    id = 'id_example' # str | 
    terminate_negotiation_v3 = openapi_client.TerminateNegotiationV3() # TerminateNegotiationV3 |  (optional)

    try:
        api_instance.terminate_negotiation_v3(id, terminate_negotiation_v3=terminate_negotiation_v3)
    except Exception as e:
        print("Exception when calling ContractNegotiationV3Api->terminate_negotiation_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **terminate_negotiation_v3** | [**TerminateNegotiationV3**](TerminateNegotiationV3.md)|  | [optional] 

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
**200** | ContractNegotiation is terminating |  -  |
**400** | Request was malformed |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

