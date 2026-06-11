# openapi_client.PolicyDefinitionV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution_plan_v4**](PolicyDefinitionV4Api.md#create_execution_plan_v4) | **POST** /v4/policydefinitions/{id}/evaluationplan | 
[**create_policy_definition_v4**](PolicyDefinitionV4Api.md#create_policy_definition_v4) | **POST** /v4/policydefinitions | 
[**delete_policy_definition_v4**](PolicyDefinitionV4Api.md#delete_policy_definition_v4) | **DELETE** /v4/policydefinitions/{id} | 
[**get_policy_definition_v4**](PolicyDefinitionV4Api.md#get_policy_definition_v4) | **GET** /v4/policydefinitions/{id} | 
[**query_policy_definitions_v4**](PolicyDefinitionV4Api.md#query_policy_definitions_v4) | **POST** /v4/policydefinitions/request | 
[**update_policy_definition_v4**](PolicyDefinitionV4Api.md#update_policy_definition_v4) | **PUT** /v4/policydefinitions/{id} | 
[**validate_policy_definition_v4**](PolicyDefinitionV4Api.md#validate_policy_definition_v4) | **POST** /v4/policydefinitions/{id}/validate | 


# **create_execution_plan_v4**
> PolicyEvaluationPlanSchema create_execution_plan_v4(id, policy_evaluation_plan_request_schema=policy_evaluation_plan_request_schema)

Creates an execution plane for an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import openapi_client
from openapi_client.models.policy_evaluation_plan_request_schema import PolicyEvaluationPlanRequestSchema
from openapi_client.models.policy_evaluation_plan_schema import PolicyEvaluationPlanSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    id = 'id_example' # str | 
    policy_evaluation_plan_request_schema = openapi_client.PolicyEvaluationPlanRequestSchema() # PolicyEvaluationPlanRequestSchema |  (optional)

    try:
        api_response = api_instance.create_execution_plan_v4(id, policy_evaluation_plan_request_schema=policy_evaluation_plan_request_schema)
        print("The response of PolicyDefinitionV4Api->create_execution_plan_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->create_execution_plan_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy_evaluation_plan_request_schema** | [**PolicyEvaluationPlanRequestSchema**](PolicyEvaluationPlanRequestSchema.md)|  | [optional] 

### Return type

[**PolicyEvaluationPlanSchema**](PolicyEvaluationPlanSchema.md)

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

# **create_policy_definition_v4**
> IdResponseSchema create_policy_definition_v4(policy_definition_schema=policy_definition_schema)

Creates a new policy definition

### Example


```python
import openapi_client
from openapi_client.models.id_response_schema import IdResponseSchema
from openapi_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    policy_definition_schema = openapi_client.PolicyDefinitionSchema() # PolicyDefinitionSchema |  (optional)

    try:
        api_response = api_instance.create_policy_definition_v4(policy_definition_schema=policy_definition_schema)
        print("The response of PolicyDefinitionV4Api->create_policy_definition_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->create_policy_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_definition_schema** | [**PolicyDefinitionSchema**](PolicyDefinitionSchema.md)|  | [optional] 

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
**200** | policy definition was created successfully. Returns the Policy Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create policy definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_definition_v4**
> delete_policy_definition_v4(id)

Removes a policy definition with the given ID if possible. Deleting a policy definition is only possible if that policy definition is not yet referenced by a contract definition, in which case an error is returned. DANGER ZONE: Note that deleting policy definitions can have unexpected results, do this at your own risk!

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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_policy_definition_v4(id)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->delete_policy_definition_v4: %s\n" % e)
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

# **get_policy_definition_v4**
> PolicyDefinitionSchema get_policy_definition_v4(id)

Gets a policy definition with the given ID

### Example


```python
import openapi_client
from openapi_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policy_definition_v4(id)
        print("The response of PolicyDefinitionV4Api->get_policy_definition_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->get_policy_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyDefinitionSchema**](PolicyDefinitionSchema.md)

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

# **query_policy_definitions_v4**
> List[PolicyDefinitionSchema] query_policy_definitions_v4(query_spec_schema=query_spec_schema)

Returns all policy definitions according to a query

### Example


```python
import openapi_client
from openapi_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_policy_definitions_v4(query_spec_schema=query_spec_schema)
        print("The response of PolicyDefinitionV4Api->query_policy_definitions_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->query_policy_definitions_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[PolicyDefinitionSchema]**](PolicyDefinitionSchema.md)

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

# **update_policy_definition_v4**
> update_policy_definition_v4(id, policy_definition_schema=policy_definition_schema)

Updates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import openapi_client
from openapi_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    id = 'id_example' # str | 
    policy_definition_schema = openapi_client.PolicyDefinitionSchema() # PolicyDefinitionSchema |  (optional)

    try:
        api_instance.update_policy_definition_v4(id, policy_definition_schema=policy_definition_schema)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->update_policy_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy_definition_schema** | [**PolicyDefinitionSchema**](PolicyDefinitionSchema.md)|  | [optional] 

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

# **validate_policy_definition_v4**
> PolicyValidationResultSchema validate_policy_definition_v4(id)

Validates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import openapi_client
from openapi_client.models.policy_validation_result_schema import PolicyValidationResultSchema
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
    api_instance = openapi_client.PolicyDefinitionV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.validate_policy_definition_v4(id)
        print("The response of PolicyDefinitionV4Api->validate_policy_definition_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV4Api->validate_policy_definition_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyValidationResultSchema**](PolicyValidationResultSchema.md)

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

