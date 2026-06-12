# edc_client.PolicyDefinitionV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution_plan_v5**](PolicyDefinitionV5betaApi.md#create_execution_plan_v5) | **POST** /v5beta/participants/{participantContextId}/policydefinitions/{id}/evaluationplan | 
[**create_policy_definition_v5**](PolicyDefinitionV5betaApi.md#create_policy_definition_v5) | **POST** /v5beta/participants/{participantContextId}/policydefinitions | 
[**delete_policy_definition_v5**](PolicyDefinitionV5betaApi.md#delete_policy_definition_v5) | **DELETE** /v5beta/participants/{participantContextId}/policydefinitions/{id} | 
[**get_policy_definition_v5**](PolicyDefinitionV5betaApi.md#get_policy_definition_v5) | **GET** /v5beta/participants/{participantContextId}/policydefinitions/{id} | 
[**query_policy_definitions_v5**](PolicyDefinitionV5betaApi.md#query_policy_definitions_v5) | **POST** /v5beta/participants/{participantContextId}/policydefinitions/request | 
[**update_policy_definition_v5**](PolicyDefinitionV5betaApi.md#update_policy_definition_v5) | **PUT** /v5beta/participants/{participantContextId}/policydefinitions/{id} | 
[**validate_policy_definition_v5**](PolicyDefinitionV5betaApi.md#validate_policy_definition_v5) | **POST** /v5beta/participants/{participantContextId}/policydefinitions/{id}/validate | 


# **create_execution_plan_v5**
> PolicyEvaluationPlanSchema create_execution_plan_v5(participant_context_id, id, policy_evaluation_plan_request_schema=policy_evaluation_plan_request_schema)

Creates an execution plane for an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_evaluation_plan_request_schema import PolicyEvaluationPlanRequestSchema
from edc_client.models.policy_evaluation_plan_schema import PolicyEvaluationPlanSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 
    policy_evaluation_plan_request_schema = edc_client.PolicyEvaluationPlanRequestSchema() # PolicyEvaluationPlanRequestSchema |  (optional)

    try:
        api_response = api_instance.create_execution_plan_v5(participant_context_id, id, policy_evaluation_plan_request_schema=policy_evaluation_plan_request_schema)
        print("The response of PolicyDefinitionV5betaApi->create_execution_plan_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->create_execution_plan_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **create_policy_definition_v5**
> IdResponseSchema create_policy_definition_v5(participant_context_id, policy_definition_schema=policy_definition_schema)

Creates a new policy definition

### Example


```python
import edc_client
from edc_client.models.id_response_schema import IdResponseSchema
from edc_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    policy_definition_schema = edc_client.PolicyDefinitionSchema() # PolicyDefinitionSchema |  (optional)

    try:
        api_response = api_instance.create_policy_definition_v5(participant_context_id, policy_definition_schema=policy_definition_schema)
        print("The response of PolicyDefinitionV5betaApi->create_policy_definition_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->create_policy_definition_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **delete_policy_definition_v5**
> delete_policy_definition_v5(participant_context_id, id)

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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_instance.delete_policy_definition_v5(participant_context_id, id)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->delete_policy_definition_v5: %s\n" % e)
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
**204** | Policy definition was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An policy definition with the given ID does not exist |  -  |
**409** | The policy definition cannot be deleted, because it is referenced by a contract definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_definition_v5**
> PolicyDefinitionSchema get_policy_definition_v5(participant_context_id, id)

Gets a policy definition with the given ID

### Example


```python
import edc_client
from edc_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policy_definition_v5(participant_context_id, id)
        print("The response of PolicyDefinitionV5betaApi->get_policy_definition_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->get_policy_definition_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **query_policy_definitions_v5**
> List[PolicyDefinitionSchema] query_policy_definitions_v5(participant_context_id, query_spec_schema=query_spec_schema)

Returns all policy definitions according to a query

### Example


```python
import edc_client
from edc_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    query_spec_schema = edc_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_policy_definitions_v5(participant_context_id, query_spec_schema=query_spec_schema)
        print("The response of PolicyDefinitionV5betaApi->query_policy_definitions_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->query_policy_definitions_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **update_policy_definition_v5**
> update_policy_definition_v5(participant_context_id, id, policy_definition_schema=policy_definition_schema)

Updates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_definition_schema import PolicyDefinitionSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 
    policy_definition_schema = edc_client.PolicyDefinitionSchema() # PolicyDefinitionSchema |  (optional)

    try:
        api_instance.update_policy_definition_v5(participant_context_id, id, policy_definition_schema=policy_definition_schema)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->update_policy_definition_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **validate_policy_definition_v5**
> PolicyValidationResultSchema validate_policy_definition_v5(participant_context_id, id)

Validates an existing Policy, If the Policy is not found, an error is reported

### Example


```python
import edc_client
from edc_client.models.policy_validation_result_schema import PolicyValidationResultSchema
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
    api_instance = edc_client.PolicyDefinitionV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.validate_policy_definition_v5(participant_context_id, id)
        print("The response of PolicyDefinitionV5betaApi->validate_policy_definition_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionV5betaApi->validate_policy_definition_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

