# openapi_client.ContractDefinitionV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract_definition_v3**](ContractDefinitionV3Api.md#create_contract_definition_v3) | **POST** /v3/contractdefinitions | 
[**delete_contract_definition_v3**](ContractDefinitionV3Api.md#delete_contract_definition_v3) | **DELETE** /v3/contractdefinitions/{id} | 
[**get_contract_definition_v3**](ContractDefinitionV3Api.md#get_contract_definition_v3) | **GET** /v3/contractdefinitions/{id} | 
[**query_contract_definitions_v3**](ContractDefinitionV3Api.md#query_contract_definitions_v3) | **POST** /v3/contractdefinitions/request | 
[**update_contract_definition_v3**](ContractDefinitionV3Api.md#update_contract_definition_v3) | **PUT** /v3/contractdefinitions | 


# **create_contract_definition_v3**
> IdResponse create_contract_definition_v3(contract_definition_input_v3=contract_definition_input_v3)

Creates a new contract definition

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_input_v3 import ContractDefinitionInputV3
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
    api_instance = openapi_client.ContractDefinitionV3Api(api_client)
    contract_definition_input_v3 = openapi_client.ContractDefinitionInputV3() # ContractDefinitionInputV3 |  (optional)

    try:
        api_response = api_instance.create_contract_definition_v3(contract_definition_input_v3=contract_definition_input_v3)
        print("The response of ContractDefinitionV3Api->create_contract_definition_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV3Api->create_contract_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_input_v3** | [**ContractDefinitionInputV3**](ContractDefinitionInputV3.md)|  | [optional] 

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
**200** | contract definition was created successfully. Returns the Contract Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create contract definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_definition_v3**
> delete_contract_definition_v3(id)

Removes a contract definition with the given ID if possible. DANGER ZONE: Note that deleting contract definitions can have unexpected results, especially for contract offers that have been sent out or ongoing or contract negotiations.

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
    api_instance = openapi_client.ContractDefinitionV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_contract_definition_v3(id)
    except Exception as e:
        print("Exception when calling ContractDefinitionV3Api->delete_contract_definition_v3: %s\n" % e)
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
**204** | Contract definition was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_definition_v3**
> ContractDefinitionOutputV3 get_contract_definition_v3(id)

Gets an contract definition with the given ID

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_output_v3 import ContractDefinitionOutputV3
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
    api_instance = openapi_client.ContractDefinitionV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_contract_definition_v3(id)
        print("The response of ContractDefinitionV3Api->get_contract_definition_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV3Api->get_contract_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractDefinitionOutputV3**](ContractDefinitionOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract definition |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract agreement with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_contract_definitions_v3**
> List[ContractDefinitionOutputV3] query_contract_definitions_v3(query_spec=query_spec)

Returns all contract definitions according to a query

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_output_v3 import ContractDefinitionOutputV3
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
    api_instance = openapi_client.ContractDefinitionV3Api(api_client)
    query_spec = openapi_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.query_contract_definitions_v3(query_spec=query_spec)
        print("The response of ContractDefinitionV3Api->query_contract_definitions_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV3Api->query_contract_definitions_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[ContractDefinitionOutputV3]**](ContractDefinitionOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract definitions matching the query |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract_definition_v3**
> update_contract_definition_v3(contract_definition_input_v3=contract_definition_input_v3)

Updated a contract definition with the given ID. The supplied JSON structure must be a valid JSON-LD object

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_input_v3 import ContractDefinitionInputV3
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
    api_instance = openapi_client.ContractDefinitionV3Api(api_client)
    contract_definition_input_v3 = openapi_client.ContractDefinitionInputV3() # ContractDefinitionInputV3 |  (optional)

    try:
        api_instance.update_contract_definition_v3(contract_definition_input_v3=contract_definition_input_v3)
    except Exception as e:
        print("Exception when calling ContractDefinitionV3Api->update_contract_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_input_v3** | [**ContractDefinitionInputV3**](ContractDefinitionInputV3.md)|  | [optional] 

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
**204** | Contract definition was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

