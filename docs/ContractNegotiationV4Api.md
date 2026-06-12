# edc_client.ContractNegotiationV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_negotiation_v4**](ContractNegotiationV4Api.md#delete_negotiation_v4) | **DELETE** /v4/contractnegotiations/{id} | 
[**get_agreement_for_negotiation_v4**](ContractNegotiationV4Api.md#get_agreement_for_negotiation_v4) | **GET** /v4/contractnegotiations/{id}/agreement | 
[**get_negotiation_state_v4**](ContractNegotiationV4Api.md#get_negotiation_state_v4) | **GET** /v4/contractnegotiations/{id}/state | 
[**get_negotiation_v4**](ContractNegotiationV4Api.md#get_negotiation_v4) | **GET** /v4/contractnegotiations/{id} | 
[**initiate_contract_negotiation_v4**](ContractNegotiationV4Api.md#initiate_contract_negotiation_v4) | **POST** /v4/contractnegotiations | 
[**query_negotiations_v4**](ContractNegotiationV4Api.md#query_negotiations_v4) | **POST** /v4/contractnegotiations/request | 
[**terminate_negotiation_v4**](ContractNegotiationV4Api.md#terminate_negotiation_v4) | **POST** /v4/contractnegotiations/{id}/terminate | 


# **delete_negotiation_v4**
> delete_negotiation_v4(id)

Deletes the contract negotiation with the given ID. Only terminated negotiations without agreement will be deleted

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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_negotiation_v4(id)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->delete_negotiation_v4: %s\n" % e)
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

# **get_agreement_for_negotiation_v4**
> ContractAgreementSchema get_agreement_for_negotiation_v4(id)

Gets a contract agreement for a contract negotiation with the given ID

### Example


```python
import edc_client
from edc_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_for_negotiation_v4(id)
        print("The response of ContractNegotiationV4Api->get_agreement_for_negotiation_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->get_agreement_for_negotiation_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractAgreementSchema**](ContractAgreementSchema.md)

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

# **get_negotiation_state_v4**
> NegotiationState get_negotiation_state_v4(id)

Gets the state of a contract negotiation with the given ID

### Example


```python
import edc_client
from edc_client.models.negotiation_state import NegotiationState
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_state_v4(id)
        print("The response of ContractNegotiationV4Api->get_negotiation_state_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->get_negotiation_state_v4: %s\n" % e)
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

# **get_negotiation_v4**
> ContractNegotiationSchema get_negotiation_v4(id)

Gets a contract negotiation with the given ID

### Example


```python
import edc_client
from edc_client.models.contract_negotiation_schema import ContractNegotiationSchema
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_v4(id)
        print("The response of ContractNegotiationV4Api->get_negotiation_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->get_negotiation_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractNegotiationSchema**](ContractNegotiationSchema.md)

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

# **initiate_contract_negotiation_v4**
> IdResponseSchema initiate_contract_negotiation_v4(contract_request_schema=contract_request_schema)

Initiates a contract negotiation for a given offer and with the given counter part. Please note that successfully invoking this endpoint only means that the negotiation was initiated. Clients must poll the /{id}/state endpoint to track the state

### Example


```python
import edc_client
from edc_client.models.contract_request_schema import ContractRequestSchema
from edc_client.models.id_response_schema import IdResponseSchema
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    contract_request_schema = edc_client.ContractRequestSchema() # ContractRequestSchema |  (optional)

    try:
        api_response = api_instance.initiate_contract_negotiation_v4(contract_request_schema=contract_request_schema)
        print("The response of ContractNegotiationV4Api->initiate_contract_negotiation_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->initiate_contract_negotiation_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_request_schema** | [**ContractRequestSchema**](ContractRequestSchema.md)|  | [optional] 

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
**200** | The negotiation was successfully initiated. Returns the contract negotiation ID and created timestamp |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_negotiations_v4**
> List[ContractNegotiationSchema] query_negotiations_v4(query_spec_schema=query_spec_schema)

Returns all contract negotiations according to a query

### Example


```python
import edc_client
from edc_client.models.contract_negotiation_schema import ContractNegotiationSchema
from edc_client.models.query_spec_schema import QuerySpecSchema
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    query_spec_schema = edc_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_negotiations_v4(query_spec_schema=query_spec_schema)
        print("The response of ContractNegotiationV4Api->query_negotiations_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->query_negotiations_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[ContractNegotiationSchema]**](ContractNegotiationSchema.md)

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

# **terminate_negotiation_v4**
> terminate_negotiation_v4(id, contract_terminate_schema=contract_terminate_schema)

Terminates the contract negotiation.

### Example


```python
import edc_client
from edc_client.models.contract_terminate_schema import ContractTerminateSchema
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
    api_instance = edc_client.ContractNegotiationV4Api(api_client)
    id = 'id_example' # str | 
    contract_terminate_schema = edc_client.ContractTerminateSchema() # ContractTerminateSchema |  (optional)

    try:
        api_instance.terminate_negotiation_v4(id, contract_terminate_schema=contract_terminate_schema)
    except Exception as e:
        print("Exception when calling ContractNegotiationV4Api->terminate_negotiation_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **contract_terminate_schema** | [**ContractTerminateSchema**](ContractTerminateSchema.md)|  | [optional] 

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

