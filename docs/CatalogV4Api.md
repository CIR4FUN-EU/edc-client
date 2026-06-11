# openapi_client.CatalogV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_v4**](CatalogV4Api.md#get_dataset_v4) | **POST** /v4/catalog/dataset/request | 
[**request_catalog_v4**](CatalogV4Api.md#request_catalog_v4) | **POST** /v4/catalog/request | 


# **get_dataset_v4**
> DatasetSchema get_dataset_v4(catalog_request_schema=catalog_request_schema)

### Example


```python
import openapi_client
from openapi_client.models.catalog_request_schema import CatalogRequestSchema
from openapi_client.models.dataset_schema import DatasetSchema
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
    api_instance = openapi_client.CatalogV4Api(api_client)
    catalog_request_schema = openapi_client.CatalogRequestSchema() # CatalogRequestSchema |  (optional)

    try:
        api_response = api_instance.get_dataset_v4(catalog_request_schema=catalog_request_schema)
        print("The response of CatalogV4Api->get_dataset_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV4Api->get_dataset_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_request_schema** | [**CatalogRequestSchema**](CatalogRequestSchema.md)|  | [optional] 

### Return type

[**DatasetSchema**](DatasetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Gets single dataset from a connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_catalog_v4**
> CatalogSchema request_catalog_v4(catalog_request_schema=catalog_request_schema)

### Example


```python
import openapi_client
from openapi_client.models.catalog_request_schema import CatalogRequestSchema
from openapi_client.models.catalog_schema import CatalogSchema
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
    api_instance = openapi_client.CatalogV4Api(api_client)
    catalog_request_schema = openapi_client.CatalogRequestSchema() # CatalogRequestSchema |  (optional)

    try:
        api_response = api_instance.request_catalog_v4(catalog_request_schema=catalog_request_schema)
        print("The response of CatalogV4Api->request_catalog_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV4Api->request_catalog_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_request_schema** | [**CatalogRequestSchema**](CatalogRequestSchema.md)|  | [optional] 

### Return type

[**CatalogSchema**](CatalogSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Gets contract offers (&#x3D;catalog) of a single connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

