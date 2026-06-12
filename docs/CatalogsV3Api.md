# edc_client.CatalogsV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_catalogs_v3**](CatalogsV3Api.md#request_catalogs_v3) | **POST** /v3/catalogs/request | 


# **request_catalogs_v3**
> List[object] request_catalogs_v3(flatten=flatten, query_spec=query_spec)

Obtains all catalogs currently held by this cache instance

### Example


```python
import edc_client
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
    api_instance = edc_client.CatalogsV3Api(api_client)
    flatten = False # bool |  (optional) (default to False)
    query_spec = edc_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.request_catalogs_v3(flatten=flatten, query_spec=query_spec)
        print("The response of CatalogsV3Api->request_catalogs_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogsV3Api->request_catalogs_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flatten** | **bool**|  | [optional] [default to False]
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of catalogs is returned, potentially empty |  -  |
**500** | A query could not be completed due to an internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

