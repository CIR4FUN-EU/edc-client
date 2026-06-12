# edc_client.AssetV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_v5**](AssetV5betaApi.md#create_asset_v5) | **POST** /v5beta/participants/{participantContextId}/assets | 
[**get_asset_v5**](AssetV5betaApi.md#get_asset_v5) | **GET** /v5beta/participants/{participantContextId}/assets/{id} | 
[**query_assets_v5**](AssetV5betaApi.md#query_assets_v5) | **POST** /v5beta/participants/{participantContextId}/assets/request | 
[**remove_asset_v5**](AssetV5betaApi.md#remove_asset_v5) | **DELETE** /v5beta/participants/{participantContextId}/assets/{assetId} | 
[**update_asset_v5**](AssetV5betaApi.md#update_asset_v5) | **PUT** /v5beta/participants/{participantContextId}/assets | 


# **create_asset_v5**
> IdResponseSchema create_asset_v5(participant_context_id, asset_schema=asset_schema)

Creates a new asset together with a data address

### Example


```python
import edc_client
from edc_client.models.asset_schema import AssetSchema
from edc_client.models.id_response_schema import IdResponseSchema
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
    api_instance = edc_client.AssetV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    asset_schema = edc_client.AssetSchema() # AssetSchema |  (optional)

    try:
        api_response = api_instance.create_asset_v5(participant_context_id, asset_schema=asset_schema)
        print("The response of AssetV5betaApi->create_asset_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV5betaApi->create_asset_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **asset_schema** | [**AssetSchema**](AssetSchema.md)|  | [optional] 

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
**200** | Asset was created successfully. Returns the asset Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create asset, because an asset with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_v5**
> AssetSchema get_asset_v5(participant_context_id, id)

Gets an asset with the given ID

### Example


```python
import edc_client
from edc_client.models.asset_schema import AssetSchema
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
    api_instance = edc_client.AssetV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_asset_v5(participant_context_id, id)
        print("The response of AssetV5betaApi->get_asset_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV5betaApi->get_asset_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**AssetSchema**](AssetSchema.md)

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

# **query_assets_v5**
> List[AssetSchema] query_assets_v5(participant_context_id, query_spec_schema=query_spec_schema)

Request all assets according to a particular query

### Example


```python
import edc_client
from edc_client.models.asset_schema import AssetSchema
from edc_client.models.query_spec_schema import QuerySpecSchema
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
    api_instance = edc_client.AssetV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    query_spec_schema = edc_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_assets_v5(participant_context_id, query_spec_schema=query_spec_schema)
        print("The response of AssetV5betaApi->query_assets_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetV5betaApi->query_assets_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[AssetSchema]**](AssetSchema.md)

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

# **remove_asset_v5**
> remove_asset_v5(participant_context_id, asset_id)

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
    api_instance = edc_client.AssetV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        api_instance.remove_asset_v5(participant_context_id, asset_id)
    except Exception as e:
        print("Exception when calling AssetV5betaApi->remove_asset_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **asset_id** | **str**|  | 

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

# **update_asset_v5**
> update_asset_v5(participant_context_id, asset_schema=asset_schema)

Updates an asset with the given ID if it exists. If the asset is not found, no further action is taken. DANGER ZONE: Note that updating assets can have unexpected results, especially for contract offers that have been sent out or are ongoing in contract negotiations.

### Example


```python
import edc_client
from edc_client.models.asset_schema import AssetSchema
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
    api_instance = edc_client.AssetV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    asset_schema = edc_client.AssetSchema() # AssetSchema |  (optional)

    try:
        api_instance.update_asset_v5(participant_context_id, asset_schema=asset_schema)
    except Exception as e:
        print("Exception when calling AssetV5betaApi->update_asset_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **asset_schema** | [**AssetSchema**](AssetSchema.md)|  | [optional] 

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

