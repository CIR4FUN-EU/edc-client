# edc_client.CatalogV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_v3**](CatalogV3Api.md#get_dataset_v3) | **POST** /v3/catalog/dataset/request | 
[**request_catalog_v3**](CatalogV3Api.md#request_catalog_v3) | **POST** /v3/catalog/request | 


# **get_dataset_v3**
> object get_dataset_v3(dataset_request_v3=dataset_request_v3)

### Example


```python
import edc_client
from edc_client.models.dataset_request_v3 import DatasetRequestV3
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
    api_instance = edc_client.CatalogV3Api(api_client)
    dataset_request_v3 = edc_client.DatasetRequestV3() # DatasetRequestV3 |  (optional)

    try:
        api_response = api_instance.get_dataset_v3(dataset_request_v3=dataset_request_v3)
        print("The response of CatalogV3Api->get_dataset_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV3Api->get_dataset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_request_v3** | [**DatasetRequestV3**](DatasetRequestV3.md)|  | [optional] 

### Return type

**object**

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

# **request_catalog_v3**
> object request_catalog_v3(catalog_request_v3=catalog_request_v3)

### Example


```python
import edc_client
from edc_client.models.catalog_request_v3 import CatalogRequestV3
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
    api_instance = edc_client.CatalogV3Api(api_client)
    catalog_request_v3 = edc_client.CatalogRequestV3() # CatalogRequestV3 |  (optional)

    try:
        api_response = api_instance.request_catalog_v3(catalog_request_v3=catalog_request_v3)
        print("The response of CatalogV3Api->request_catalog_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV3Api->request_catalog_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_request_v3** | [**CatalogRequestV3**](CatalogRequestV3.md)|  | [optional] 

### Return type

**object**

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

