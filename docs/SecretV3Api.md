# edc_client.SecretV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_v3**](SecretV3Api.md#create_secret_v3) | **POST** /v3/secrets | 
[**get_secret_v3**](SecretV3Api.md#get_secret_v3) | **GET** /v3/secrets/{id} | 
[**remove_secret_v3**](SecretV3Api.md#remove_secret_v3) | **DELETE** /v3/secrets/{id} | 
[**update_secret_v3**](SecretV3Api.md#update_secret_v3) | **PUT** /v3/secrets | 


# **create_secret_v3**
> IdResponse create_secret_v3(secret_input_v3=secret_input_v3)

Creates a new secret.

### Example


```python
import edc_client
from edc_client.models.id_response import IdResponse
from edc_client.models.secret_input_v3 import SecretInputV3
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
    api_instance = edc_client.SecretV3Api(api_client)
    secret_input_v3 = edc_client.SecretInputV3() # SecretInputV3 |  (optional)

    try:
        api_response = api_instance.create_secret_v3(secret_input_v3=secret_input_v3)
        print("The response of SecretV3Api->create_secret_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretV3Api->create_secret_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_input_v3** | [**SecretInputV3**](SecretInputV3.md)|  | [optional] 

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
**200** | Secret was created successfully. Returns the secret Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create secret, because a secret with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_v3**
> SecretOutputV3 get_secret_v3(id)

Gets a secret with the given ID

### Example


```python
import edc_client
from edc_client.models.secret_output_v3 import SecretOutputV3
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
    api_instance = edc_client.SecretV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_secret_v3(id)
        print("The response of SecretV3Api->get_secret_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretV3Api->get_secret_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SecretOutputV3**](SecretOutputV3.md)

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

# **remove_secret_v3**
> remove_secret_v3(id)

Removes a secret with the given ID if possible.

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
    api_instance = edc_client.SecretV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.remove_secret_v3(id)
    except Exception as e:
        print("Exception when calling SecretV3Api->remove_secret_v3: %s\n" % e)
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

# **update_secret_v3**
> update_secret_v3(secret_input_v3=secret_input_v3)

Updates a secret with the given ID if it exists. If the secret is not found, no further action is taken. 

### Example


```python
import edc_client
from edc_client.models.secret_input_v3 import SecretInputV3
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
    api_instance = edc_client.SecretV3Api(api_client)
    secret_input_v3 = edc_client.SecretInputV3() # SecretInputV3 |  (optional)

    try:
        api_instance.update_secret_v3(secret_input_v3=secret_input_v3)
    except Exception as e:
        print("Exception when calling SecretV3Api->update_secret_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_input_v3** | [**SecretInputV3**](SecretInputV3.md)|  | [optional] 

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

