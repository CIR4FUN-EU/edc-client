# openapi_client.SecretV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_v4**](SecretV4Api.md#create_secret_v4) | **POST** /v4/secrets | 
[**get_secret_v4**](SecretV4Api.md#get_secret_v4) | **GET** /v4/secrets/{id} | 
[**remove_secret_v4**](SecretV4Api.md#remove_secret_v4) | **DELETE** /v4/secrets/{id} | 
[**update_secret_v4**](SecretV4Api.md#update_secret_v4) | **PUT** /v4/secrets | 


# **create_secret_v4**
> IdResponseSchema create_secret_v4(secret_schema=secret_schema)

Creates a new secret.

### Example


```python
import openapi_client
from openapi_client.models.id_response_schema import IdResponseSchema
from openapi_client.models.secret_schema import SecretSchema
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
    api_instance = openapi_client.SecretV4Api(api_client)
    secret_schema = openapi_client.SecretSchema() # SecretSchema |  (optional)

    try:
        api_response = api_instance.create_secret_v4(secret_schema=secret_schema)
        print("The response of SecretV4Api->create_secret_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretV4Api->create_secret_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_schema** | [**SecretSchema**](SecretSchema.md)|  | [optional] 

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
**200** | Secret was created successfully. Returns the secret Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create secret, because a secret with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_v4**
> SecretSchema get_secret_v4(id)

Gets a secret with the given ID

### Example


```python
import openapi_client
from openapi_client.models.secret_schema import SecretSchema
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
    api_instance = openapi_client.SecretV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_secret_v4(id)
        print("The response of SecretV4Api->get_secret_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretV4Api->get_secret_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SecretSchema**](SecretSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The secret |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A secret with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_secret_v4**
> remove_secret_v4(id)

Removes a secret with the given ID if possible.

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
    api_instance = openapi_client.SecretV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.remove_secret_v4(id)
    except Exception as e:
        print("Exception when calling SecretV4Api->remove_secret_v4: %s\n" % e)
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
**204** | Secret was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A secret with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_v4**
> update_secret_v4(secret_schema=secret_schema)

Updates a secret with the given ID if it exists. If the secret is not found, no further action is taken. 

### Example


```python
import openapi_client
from openapi_client.models.secret_schema import SecretSchema
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
    api_instance = openapi_client.SecretV4Api(api_client)
    secret_schema = openapi_client.SecretSchema() # SecretSchema |  (optional)

    try:
        api_instance.update_secret_v4(secret_schema=secret_schema)
    except Exception as e:
        print("Exception when calling SecretV4Api->update_secret_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_schema** | [**SecretSchema**](SecretSchema.md)|  | [optional] 

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
**204** | Secret was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | Secret could not be updated, because it does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

