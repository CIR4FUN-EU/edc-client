# edc_client.CatalogV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_v5**](CatalogV5betaApi.md#get_dataset_v5) | **POST** /v5beta/participants/{participantContextId}/catalog/dataset/request | 
[**request_catalog_v5**](CatalogV5betaApi.md#request_catalog_v5) | **POST** /v5beta/participants/{participantContextId}/catalog/request | 


# **get_dataset_v5**
> DatasetSchema get_dataset_v5(participant_context_id, catalog_request_schema=catalog_request_schema)

### Example


```python
import edc_client
from edc_client.models.catalog_request_schema import CatalogRequestSchema
from edc_client.models.dataset_schema import DatasetSchema
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
    api_instance = edc_client.CatalogV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    catalog_request_schema = edc_client.CatalogRequestSchema() # CatalogRequestSchema |  (optional)

    try:
        api_response = api_instance.get_dataset_v5(participant_context_id, catalog_request_schema=catalog_request_schema)
        print("The response of CatalogV5betaApi->get_dataset_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV5betaApi->get_dataset_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

# **request_catalog_v5**
> CatalogSchema request_catalog_v5(participant_context_id, catalog_request_schema=catalog_request_schema)

### Example


```python
import edc_client
from edc_client.models.catalog_request_schema import CatalogRequestSchema
from edc_client.models.catalog_schema import CatalogSchema
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
    api_instance = edc_client.CatalogV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    catalog_request_schema = edc_client.CatalogRequestSchema() # CatalogRequestSchema |  (optional)

    try:
        api_response = api_instance.request_catalog_v5(participant_context_id, catalog_request_schema=catalog_request_schema)
        print("The response of CatalogV5betaApi->request_catalog_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogV5betaApi->request_catalog_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
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

