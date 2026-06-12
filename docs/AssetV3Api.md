# edc_client.AssetV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_v3**](AssetV3Api.md#create_asset_v3) | **POST** /v3/assets | 
[**get_asset_v3**](AssetV3Api.md#get_asset_v3) | **GET** /v3/assets/{id} | 
[**remove_asset_v3**](AssetV3Api.md#remove_asset_v3) | **DELETE** /v3/assets/{id} | 
[**request_assets_v3**](AssetV3Api.md#request_assets_v3) | **POST** /v3/assets/request | 
[**update_asset_v3**](AssetV3Api.md#update_asset_v3) | **PUT** /v3/assets | 


# **create_asset_v3**
> IdResponse create_asset_v3(asset_input_v3=asset_input_v3)

Creates a new asset together with a data address

### Example


```python
import edc_client
from edc_client.models.asset_input_v3 import AssetInputV3
from edc_client.models.id_response import IdResponse
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
    api_instance = edc_client.AssetV3Api(api_client)
    asset_input_v3 = edc_client.AssetInputV3() # AssetInputV3 |  (optional)

    try:
        api_response = api_instance.create_asset_v3(asset_input_v3=asset_input_v3)
        print("The response of AssetV3Api->create_asset_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV3Api->create_asset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_input_v3** | [**AssetInputV3**](AssetInputV3.md)|  | [optional] 

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
**200** | Asset was created successfully. Returns the asset Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create asset, because an asset with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_v3**
> AssetOutputV3 get_asset_v3(id)

Gets an asset with the given ID

### Example


```python
import edc_client
from edc_client.models.asset_output_v3 import AssetOutputV3
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
    api_instance = edc_client.AssetV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_asset_v3(id)
        print("The response of AssetV3Api->get_asset_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV3Api->get_asset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AssetOutputV3**](AssetOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asset |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_v3**
> remove_asset_v3(id)

Removes an asset with the given ID if possible. Deleting an asset is only possible if that asset is not yet referenced by a contract agreement, in which case an error is returned. DANGER ZONE: Note that deleting assets can have unexpected results, especially for contract offers that have been sent out or ongoing or contract negotiations.

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
    api_instance = edc_client.AssetV3Api(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.remove_asset_v3(id)
    except Exception as e:
        print("Exception when calling AssetV3Api->remove_asset_v3: %s\n" % e)
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
**204** | Asset was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |
**409** | The asset cannot be deleted, because it is referenced by a contract agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_assets_v3**
> List[AssetOutputV3] request_assets_v3(query_spec=query_spec)

Request all assets according to a particular query

### Example


```python
import edc_client
from edc_client.models.asset_output_v3 import AssetOutputV3
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
    api_instance = edc_client.AssetV3Api(api_client)
    query_spec = edc_client.QuerySpec() # QuerySpec |  (optional)

    try:
        api_response = api_instance.request_assets_v3(query_spec=query_spec)
        print("The response of AssetV3Api->request_assets_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV3Api->request_assets_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**List[AssetOutputV3]**](AssetOutputV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The assets matching the query |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_v3**
> update_asset_v3(asset_input_v3=asset_input_v3)

Updates an asset with the given ID if it exists. If the asset is not found, no further action is taken. DANGER ZONE: Note that updating assets can have unexpected results, especially for contract offers that have been sent out or are ongoing in contract negotiations.

### Example


```python
import edc_client
from edc_client.models.asset_input_v3 import AssetInputV3
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
    api_instance = edc_client.AssetV3Api(api_client)
    asset_input_v3 = edc_client.AssetInputV3() # AssetInputV3 |  (optional)

    try:
        api_instance.update_asset_v3(asset_input_v3=asset_input_v3)
    except Exception as e:
        print("Exception when calling AssetV3Api->update_asset_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_input_v3** | [**AssetInputV3**](AssetInputV3.md)|  | [optional] 

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
**204** | Asset was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | Asset could not be updated, because it does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

