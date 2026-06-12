# edc_client.ParticipantContextConfigV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_v5**](ParticipantContextConfigV5betaApi.md#get_config_v5) | **GET** /v5beta/participants/{participantContextId}/config | 
[**set_config_v5**](ParticipantContextConfigV5betaApi.md#set_config_v5) | **PUT** /v5beta/participants/{participantContextId}/config | 


# **get_config_v5**
> ParticipantContextConfigSchema get_config_v5(participant_context_id)

Gets ParticipantContexts config by ID.

### Example


```python
import edc_client
from edc_client.models.participant_context_config_schema import ParticipantContextConfigSchema
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
    api_instance = edc_client.ParticipantContextConfigV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 

    try:
        api_response = api_instance.get_config_v5(participant_context_id)
        print("The response of ParticipantContextConfigV5betaApi->get_config_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParticipantContextConfigV5betaApi->get_config_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 

### Return type

[**ParticipantContextConfigSchema**](ParticipantContextConfigSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The config of the ParticipantContext |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_config_v5**
> set_config_v5(participant_context_id, participant_context_config_schema=participant_context_config_schema)

Set ParticipantContext config.

### Example


```python
import edc_client
from edc_client.models.participant_context_config_schema import ParticipantContextConfigSchema
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
    api_instance = edc_client.ParticipantContextConfigV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    participant_context_config_schema = edc_client.ParticipantContextConfigSchema() # ParticipantContextConfigSchema |  (optional)

    try:
        api_instance.set_config_v5(participant_context_id, participant_context_config_schema=participant_context_config_schema)
    except Exception as e:
        print("Exception when calling ParticipantContextConfigV5betaApi->set_config_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **participant_context_config_schema** | [**ParticipantContextConfigSchema**](ParticipantContextConfigSchema.md)|  | [optional] 

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
**204** | The Config was set successfully |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**409** | Can&#39;t create the ParticipantContext, because a object with the same ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

