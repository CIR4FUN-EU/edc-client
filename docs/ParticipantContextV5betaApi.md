# edc_client.ParticipantContextV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_participant_v5**](ParticipantContextV5betaApi.md#create_participant_v5) | **POST** /v5beta/participants | 
[**delete_participant_v5**](ParticipantContextV5betaApi.md#delete_participant_v5) | **DELETE** /v5beta/participants/{id} | 
[**get_all_participants_v5**](ParticipantContextV5betaApi.md#get_all_participants_v5) | **GET** /v5beta/participants | 
[**get_participant_v5**](ParticipantContextV5betaApi.md#get_participant_v5) | **GET** /v5beta/participants/{id} | 
[**update_participant_v5**](ParticipantContextV5betaApi.md#update_participant_v5) | **PUT** /v5beta/participants/{id} | 


# **create_participant_v5**
> IdResponseSchema create_participant_v5(participant_context_schema=participant_context_schema)

Creates a new ParticipantContext object.

### Example


```python
import edc_client
from edc_client.models.id_response_schema import IdResponseSchema
from edc_client.models.participant_context_schema import ParticipantContextSchema
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
    api_instance = edc_client.ParticipantContextV5betaApi(api_client)
    participant_context_schema = edc_client.ParticipantContextSchema() # ParticipantContextSchema |  (optional)

    try:
        api_response = api_instance.create_participant_v5(participant_context_schema=participant_context_schema)
        print("The response of ParticipantContextV5betaApi->create_participant_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParticipantContextV5betaApi->create_participant_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_schema** | [**ParticipantContextSchema**](ParticipantContextSchema.md)|  | [optional] 

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
**201** | The ParticipantContext was created successfully, its API token is returned in the response body. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**409** | Can&#39;t create the ParticipantContext, because a object with the same ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant_v5**
> delete_participant_v5(id)

Delete a ParticipantContext.

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
    api_instance = edc_client.ParticipantContextV5betaApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_participant_v5(id)
    except Exception as e:
        print("Exception when calling ParticipantContextV5betaApi->delete_participant_v5: %s\n" % e)
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
**204** | The ParticipantContext was deleted successfully |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_participants_v5**
> List[ParticipantContextSchema] get_all_participants_v5(offset=offset, limit=limit)

Get all DID documents across all Participant Contexts. Requires elevated access.

### Example


```python
import edc_client
from edc_client.models.participant_context_schema import ParticipantContextSchema
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
    api_instance = edc_client.ParticipantContextV5betaApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        api_response = api_instance.get_all_participants_v5(offset=offset, limit=limit)
        print("The response of ParticipantContextV5betaApi->get_all_participants_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParticipantContextV5betaApi->get_all_participants_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**List[ParticipantContextSchema]**](ParticipantContextSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of ParticipantContexts. |  -  |
**400** | The query was malformed or was not understood by the server. |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_v5**
> ParticipantContextSchema get_participant_v5(id)

Gets ParticipantContexts by ID.

### Example


```python
import edc_client
from edc_client.models.participant_context_schema import ParticipantContextSchema
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
    api_instance = edc_client.ParticipantContextV5betaApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_participant_v5(id)
        print("The response of ParticipantContextV5betaApi->get_participant_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParticipantContextV5betaApi->get_participant_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ParticipantContextSchema**](ParticipantContextSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of ParticipantContexts. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A ParticipantContext with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant_v5**
> update_participant_v5(id, participant_context_schema=participant_context_schema)

Updates a ParticipantContext object.

### Example


```python
import edc_client
from edc_client.models.participant_context_schema import ParticipantContextSchema
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
    api_instance = edc_client.ParticipantContextV5betaApi(api_client)
    id = 'id_example' # str | 
    participant_context_schema = edc_client.ParticipantContextSchema() # ParticipantContextSchema |  (optional)

    try:
        api_instance.update_participant_v5(id, participant_context_schema=participant_context_schema)
    except Exception as e:
        print("Exception when calling ParticipantContextV5betaApi->update_participant_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **participant_context_schema** | [**ParticipantContextSchema**](ParticipantContextSchema.md)|  | [optional] 

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
**204** | The ParticipantContext was updated successfully. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**409** | Can&#39;t create the ParticipantContext, because a object with the same ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

