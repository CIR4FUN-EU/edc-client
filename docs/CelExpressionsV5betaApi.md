# openapi_client.CelExpressionsV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_expression_v5**](CelExpressionsV5betaApi.md#create_expression_v5) | **POST** /v5beta/celexpressions | 
[**delete_expression_v5**](CelExpressionsV5betaApi.md#delete_expression_v5) | **DELETE** /v5beta/celexpressions/{id} | 
[**get_expression_v5**](CelExpressionsV5betaApi.md#get_expression_v5) | **GET** /v5beta/celexpressions/{id} | 
[**query_expression_v5**](CelExpressionsV5betaApi.md#query_expression_v5) | **POST** /v5beta/celexpressions/request | 
[**test_expression_v5**](CelExpressionsV5betaApi.md#test_expression_v5) | **POST** /v5beta/celexpressions/test | 
[**update_expression_v5**](CelExpressionsV5betaApi.md#update_expression_v5) | **PUT** /v5beta/celexpressions/{id} | 


# **create_expression_v5**
> create_expression_v5(cel_expression_schema=cel_expression_schema)

Create a Cel Expression.

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_schema import CelExpressionSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    cel_expression_schema = openapi_client.CelExpressionSchema() # CelExpressionSchema |  (optional)

    try:
        api_instance.create_expression_v5(cel_expression_schema=cel_expression_schema)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->create_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cel_expression_schema** | [**CelExpressionSchema**](CelExpressionSchema.md)|  | [optional] 

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
**200** | The Cel Expression was created successfully |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**409** | Can&#39;t create the Cel expression, because a object with the same ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expression_v5**
> CelExpressionSchema delete_expression_v5(id)

Delete an Expression by ID.

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_schema import CelExpressionSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_expression_v5(id)
        print("The response of CelExpressionsV5betaApi->delete_expression_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->delete_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CelExpressionSchema**](CelExpressionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Cel Expression was deleted. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A Cel Expression with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expression_v5**
> CelExpressionSchema get_expression_v5(id)

Gets an Expression by ID.

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_schema import CelExpressionSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_expression_v5(id)
        print("The response of CelExpressionsV5betaApi->get_expression_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->get_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CelExpressionSchema**](CelExpressionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Cel Expression. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A Cel Expression with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_expression_v5**
> List[CelExpressionSchema] query_expression_v5(query_spec_schema=query_spec_schema)

Returns all cel expressions according to a query

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_schema import CelExpressionSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_expression_v5(query_spec_schema=query_spec_schema)
        print("The response of CelExpressionsV5betaApi->query_expression_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->query_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[CelExpressionSchema]**](CelExpressionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cel expressions matching the query |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_expression_v5**
> CelExpressionTestResponseSchema test_expression_v5(cel_expression_test_request_schema=cel_expression_test_request_schema)

Test a Cel Expression.

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_test_request_schema import CelExpressionTestRequestSchema
from openapi_client.models.cel_expression_test_response_schema import CelExpressionTestResponseSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    cel_expression_test_request_schema = openapi_client.CelExpressionTestRequestSchema() # CelExpressionTestRequestSchema |  (optional)

    try:
        api_response = api_instance.test_expression_v5(cel_expression_test_request_schema=cel_expression_test_request_schema)
        print("The response of CelExpressionsV5betaApi->test_expression_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->test_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cel_expression_test_request_schema** | [**CelExpressionTestRequestSchema**](CelExpressionTestRequestSchema.md)|  | [optional] 

### Return type

[**CelExpressionTestResponseSchema**](CelExpressionTestResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Cel Expression was tested successfully |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expression_v5**
> CelExpressionSchema update_expression_v5(id, update_expression_v5_request=update_expression_v5_request)

Update an Expression.

### Example


```python
import openapi_client
from openapi_client.models.cel_expression_schema import CelExpressionSchema
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
    api_instance = openapi_client.CelExpressionsV5betaApi(api_client)
    id = 'id_example' # str | 
    update_expression_v5_request = openapi_client.UpdateExpressionV5Request() # UpdateExpressionV5Request |  (optional)

    try:
        api_response = api_instance.update_expression_v5(id, update_expression_v5_request=update_expression_v5_request)
        print("The response of CelExpressionsV5betaApi->update_expression_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CelExpressionsV5betaApi->update_expression_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_expression_v5_request** | [**UpdateExpressionV5Request**](UpdateExpressionV5Request.md)|  | [optional] 

### Return type

[**CelExpressionSchema**](CelExpressionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Cel Expression was updated successfully. |  -  |
**400** | Request body was malformed, or the request could not be processed |  -  |
**401** | The request could not be completed, because either the authentication was missing or was not valid. |  -  |
**404** | A Cel Expression with the given ID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

