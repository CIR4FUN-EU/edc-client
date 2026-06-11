# openapi_client.CatalogsV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_catalogs_v4**](CatalogsV4Api.md#request_catalogs_v4) | **POST** /v4/catalogs/request | 


# **request_catalogs_v4**
> List[CatalogSchema] request_catalogs_v4(flatten=flatten, query_spec_schema=query_spec_schema)

Obtains all catalogs currently held by this cache instance

### Example


```python
import openapi_client
from openapi_client.models.catalog_schema import CatalogSchema
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
    api_instance = openapi_client.CatalogsV4Api(api_client)
    flatten = False # bool |  (optional) (default to False)
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.request_catalogs_v4(flatten=flatten, query_spec_schema=query_spec_schema)
        print("The response of CatalogsV4Api->request_catalogs_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogsV4Api->request_catalogs_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flatten** | **bool**|  | [optional] [default to False]
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[CatalogSchema]**](CatalogSchema.md)

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

