# openapi_client.ContractDefinitionV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract_definition_v4**](ContractDefinitionV4Api.md#create_contract_definition_v4) | **POST** /v4/contractdefinitions | 
[**delete_contract_definition_v4**](ContractDefinitionV4Api.md#delete_contract_definition_v4) | **DELETE** /v4/contractdefinitions/{id} | 
[**get_contract_definition_v4**](ContractDefinitionV4Api.md#get_contract_definition_v4) | **GET** /v4/contractdefinitions/{id} | 
[**query_contract_definitions_v4**](ContractDefinitionV4Api.md#query_contract_definitions_v4) | **POST** /v4/contractdefinitions/request | 
[**update_contract_definition_v4**](ContractDefinitionV4Api.md#update_contract_definition_v4) | **PUT** /v4/contractdefinitions | 


# **create_contract_definition_v4**
> IdResponseSchema create_contract_definition_v4(contract_definition_schema=contract_definition_schema)

Creates a new contract definition

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_schema import ContractDefinitionSchema
from openapi_client.models.id_response_schema import IdResponseSchema
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
    api_instance = openapi_client.ContractDefinitionV4Api(api_client)
    contract_definition_schema = openapi_client.ContractDefinitionSchema() # ContractDefinitionSchema |  (optional)

    try:
        api_response = api_instance.create_contract_definition_v4(contract_definition_schema=contract_definition_schema)
        print("The response of ContractDefinitionV4Api->create_contract_definition_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV4Api->create_contract_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_schema** | [**ContractDefinitionSchema**](ContractDefinitionSchema.md)|  | [optional] 

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
**200** | contract definition was created successfully. Returns the Contract Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create contract definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_definition_v4**
> delete_contract_definition_v4(id)

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
    api_instance = openapi_client.ContractDefinitionV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_contract_definition_v4(id)
    except Exception as e:
        print("Exception when calling ContractDefinitionV4Api->delete_contract_definition_v4: %s\n" % e)
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

# **get_contract_definition_v4**
> ContractDefinitionSchema get_contract_definition_v4(id)

Gets an contract definition with the given ID

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_schema import ContractDefinitionSchema
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
    api_instance = openapi_client.ContractDefinitionV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_contract_definition_v4(id)
        print("The response of ContractDefinitionV4Api->get_contract_definition_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV4Api->get_contract_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractDefinitionSchema**](ContractDefinitionSchema.md)

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

# **query_contract_definitions_v4**
> List[ContractDefinitionSchema] query_contract_definitions_v4(query_spec_schema=query_spec_schema)

Returns all contract definitions according to a query

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_schema import ContractDefinitionSchema
from openapi_client.models.query_spec_schema import QuerySpecSchema
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
    api_instance = openapi_client.ContractDefinitionV4Api(api_client)
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_contract_definitions_v4(query_spec_schema=query_spec_schema)
        print("The response of ContractDefinitionV4Api->query_contract_definitions_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionV4Api->query_contract_definitions_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[ContractDefinitionSchema]**](ContractDefinitionSchema.md)

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

# **update_contract_definition_v4**
> update_contract_definition_v4(contract_definition_schema=contract_definition_schema)

Updated a contract definition with the given ID. The supplied JSON structure must be a valid JSON-LD object

### Example


```python
import openapi_client
from openapi_client.models.contract_definition_schema import ContractDefinitionSchema
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
    api_instance = openapi_client.ContractDefinitionV4Api(api_client)
    contract_definition_schema = openapi_client.ContractDefinitionSchema() # ContractDefinitionSchema |  (optional)

    try:
        api_instance.update_contract_definition_v4(contract_definition_schema=contract_definition_schema)
    except Exception as e:
        print("Exception when calling ContractDefinitionV4Api->update_contract_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_schema** | [**ContractDefinitionSchema**](ContractDefinitionSchema.md)|  | [optional] 

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

