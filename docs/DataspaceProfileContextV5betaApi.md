# openapi_client.DataspaceProfileContextV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_profiles**](DataspaceProfileContextV5betaApi.md#associate_profiles) | **PUT** /v5beta/participants/{participantContextId}/profiles | 
[**get_profiles_v5**](DataspaceProfileContextV5betaApi.md#get_profiles_v5) | **GET** /v5beta/participants/{participantContextId}/profiles | 


# **associate_profiles**
> DataspaceProfileSchema associate_profiles(participant_context_id, update_expression_v5_request=update_expression_v5_request)

Associate Dataspace Profile contexts to a participant context.

### Example


```python
import openapi_client
from openapi_client.models.dataspace_profile_schema import DataspaceProfileSchema
from openapi_client.models.update_expression_v5_request import UpdateExpressionV5Request
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
    api_instance = openapi_client.DataspaceProfileContextV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    update_expression_v5_request = openapi_client.UpdateExpressionV5Request() # UpdateExpressionV5Request |  (optional)

    try:
        api_response = api_instance.associate_profiles(participant_context_id, update_expression_v5_request=update_expression_v5_request)
        print("The response of DataspaceProfileContextV5betaApi->associate_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataspaceProfileContextV5betaApi->associate_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **update_expression_v5_request** | [**UpdateExpressionV5Request**](UpdateExpressionV5Request.md)|  | [optional] 

### Return type

[**DataspaceProfileSchema**](DataspaceProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dataspace profile contexts was successfully associated to the participant context |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiles_v5**
> DataspaceProfileSchema get_profiles_v5(participant_context_id)

Gets Dataspace Profile contexts configured for the participant context id.

### Example


```python
import openapi_client
from openapi_client.models.dataspace_profile_schema import DataspaceProfileSchema
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
    api_instance = openapi_client.DataspaceProfileContextV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 

    try:
        api_response = api_instance.get_profiles_v5(participant_context_id)
        print("The response of DataspaceProfileContextV5betaApi->get_profiles_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataspaceProfileContextV5betaApi->get_profiles_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 

### Return type

[**DataspaceProfileSchema**](DataspaceProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dataspace profile contexts of the participant |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

