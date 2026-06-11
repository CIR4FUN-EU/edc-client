# openapi_client.DataplaneSelectorV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_data_plane_instances_v3**](DataplaneSelectorV3Api.md#get_all_data_plane_instances_v3) | **GET** /v3/dataplanes | 


# **get_all_data_plane_instances_v3**
> List[DataPlaneInstanceSchemaV3] get_all_data_plane_instances_v3()

Returns a list of all currently registered data plane instances

### Example


```python
import openapi_client
from openapi_client.models.data_plane_instance_schema_v3 import DataPlaneInstanceSchemaV3
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
    api_instance = openapi_client.DataplaneSelectorV3Api(api_client)

    try:
        api_response = api_instance.get_all_data_plane_instances_v3()
        print("The response of DataplaneSelectorV3Api->get_all_data_plane_instances_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataplaneSelectorV3Api->get_all_data_plane_instances_v3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DataPlaneInstanceSchemaV3]**](DataPlaneInstanceSchemaV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A (potentially empty) list of currently registered data plane instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

