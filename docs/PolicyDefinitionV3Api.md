# edc_client.PolicyDefinitionV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution_plane_v3**](PolicyDefinitionV3Api.md#create_execution_plane_v3) | **POST** /v3/policydefinitions/{id}/evaluationplan | 
[**create_policy_definition_v3**](PolicyDefinitionV3Api.md#create_policy_definition_v3) | **POST** /v3/policydefinitions | 
[**delete_policy_definition_v3**](PolicyDefinitionV3Api.md#delete_policy_definition_v3) | **DELETE** /v3/policydefinitions/{id} | 
[**get_policy_definition_v3**](PolicyDefinitionV3Api.md#get_policy_definition_v3) | **GET** /v3/policydefinitions/{id} | 
[**query_policy_definitions_v3**](PolicyDefinitionV3Api.md#query_policy_definitions_v3) | **POST** /v3/policydefinitions/request | 
[**update_policy_definition_v3**](PolicyDefinitionV3Api.md#update_policy_definition_v3) | **PUT** /v3/policydefinitions/{id} | 
[**validate_policy_definition_v3**](PolicyDefinitionV3Api.md#validate_policy_definition_v3) | **POST** /v3/policydefinitions/{id}/validate | 


# **create_execution_plane_v3**
> object create_execution_plane_v3(id, policy_evaluation_plan_request_schema_v3=policy_evaluation_plan_request_schema_v3)

Creates an execution plane for an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_evaluation_plan_request_schema_v3 import PolicyEvaluationPlanRequestSchemaV3
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    id = 'id_example' # str | 
    policy_evaluation_plan_request_schema_v3 = edc_client.PolicyEvaluationPlanRequestSchemaV3() # PolicyEvaluationPlanRequestSchemaV3 |  (optional)

    try:
        api_response = api_instance.create_execution_plane_v3(id, policy_evaluation_plan_request_schema_v3=policy_evaluation_plan_request_schema_v3)
        print("The response of PolicyDefinitionV3Api->create_execution_plane_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->create_execution_plane_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy_evaluation_plan_request_schema_v3** | [**PolicyEvaluationPlanRequestSchemaV3**](PolicyEvaluationPlanRequestSchemaV3.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the evaluation plan |  -  |
**404** | An evaluation plan could not be created, because the policy definition does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_definition_v3**
> IdResponse create_policy_definition_v3(policy_definition_input_v3=policy_definition_input_v3)

Creates a new policy definition

### Example


```python
import edc_client
from edc_client.models.id_response import IdResponse
from edc_client.models.policy_definition_input_v3 import PolicyDefinitionInputV3
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    policy_definition_input_v3 = edc_client.PolicyDefinitionInputV3() # PolicyDefinitionInputV3 |  (optional)

    try:
        api_response = api_instance.create_policy_definition_v3(policy_definition_input_v3=policy_definition_input_v3)
        print("The response of PolicyDefinitionV3Api->create_policy_definition_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->create_policy_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_definition_input_v3** | [**PolicyDefinitionInputV3**](PolicyDefinitionInputV3.md)|  | [optional] 

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
**200** | policy definition was created successfully. Returns the Policy Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create policy definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_definition_v3**
> delete_policy_definition_v3(id)

Removes a policy definition with the given ID if possible. Deleting a policy definition is only possible if that policy definition is not yet referenced by a contract definition, in which case an error is returned. DANGER ZONE: Note that deleting policy definitions can have unexpected results, do this at your own risk!

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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_policy_definition_v3(id)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->delete_policy_definition_v3: %s\n" % e)
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
**204** | Policy definition was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An policy definition with the given ID does not exist |  -  |
**409** | The policy definition cannot be deleted, because it is referenced by a contract definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_definition_v3**
> PolicyDefinitionOutputV3 get_policy_definition_v3(id)

Gets a policy definition with the given ID

### Example


```python
import edc_client
from edc_client.models.policy_definition_output_v3 import PolicyDefinitionOutputV3
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policy_definition_v3(id)
        print("The response of PolicyDefinitionV3Api->get_policy_definition_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->get_policy_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyDefinitionOutputV3**](PolicyDefinitionOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The  policy definition |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An  policy definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_policy_definitions_v3**
> List[PolicyDefinitionOutputV3] query_policy_definitions_v3(query_spec=query_spec)

Returns all policy definitions according to a query

### Example


```python
import edc_client
from edc_client.models.policy_definition_output_v3 import PolicyDefinitionOutputV3
from edc_client.models.query_spec import QuerySpec
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    query_spec = edc_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.query_policy_definitions_v3(query_spec=query_spec)
        print("The response of PolicyDefinitionV3Api->query_policy_definitions_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->query_policy_definitions_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[PolicyDefinitionOutputV3]**](PolicyDefinitionOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The policy definitions matching the query |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_definition_v3**
> update_policy_definition_v3(id, policy_definition_input_v3=policy_definition_input_v3)

Updates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_definition_input_v3 import PolicyDefinitionInputV3
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    id = 'id_example' # str | 
    policy_definition_input_v3 = edc_client.PolicyDefinitionInputV3() # PolicyDefinitionInputV3 |  (optional)

    try:
        api_instance.update_policy_definition_v3(id, policy_definition_input_v3=policy_definition_input_v3)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->update_policy_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy_definition_input_v3** | [**PolicyDefinitionInputV3**](PolicyDefinitionInputV3.md)|  | [optional] 

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
**204** | policy definition was updated successfully. |  -  |
**400** | Request body was malformed |  -  |
**404** | policy definition could not be updated, because it does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_policy_definition_v3**
> PolicyValidationResultSchemaV3 validate_policy_definition_v3(id)

Validates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_validation_result_schema_v3 import PolicyValidationResultSchemaV3
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
    api_instance = edc_client.PolicyDefinitionV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.validate_policy_definition_v3(id)
        print("The response of PolicyDefinitionV3Api->validate_policy_definition_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV3Api->validate_policy_definition_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyValidationResultSchemaV3**](PolicyValidationResultSchemaV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the validation result |  -  |
**404** | policy definition could not be validated, because it does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

