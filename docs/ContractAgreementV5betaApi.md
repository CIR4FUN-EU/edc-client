# openapi_client.ContractAgreementV5betaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agreement_by_id_v5**](ContractAgreementV5betaApi.md#get_agreement_by_id_v5) | **GET** /v5beta/participants/{participantContextId}/contractagreements/{id} | 
[**get_negotiation_by_agreement_id_v5**](ContractAgreementV5betaApi.md#get_negotiation_by_agreement_id_v5) | **GET** /v5beta/participants/{participantContextId}/contractagreements/{id}/negotiation | 
[**query_agreements_v5**](ContractAgreementV5betaApi.md#query_agreements_v5) | **POST** /v5beta/participants/{participantContextId}/contractagreements/request | 


# **get_agreement_by_id_v5**
> ContractAgreementSchema get_agreement_by_id_v5(participant_context_id, id)

Gets an contract agreement with the given ID

### Example


```python
import openapi_client
from openapi_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = openapi_client.ContractAgreementV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_by_id_v5(participant_context_id, id)
        print("The response of ContractAgreementV5betaApi->get_agreement_by_id_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV5betaApi->get_agreement_by_id_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ContractAgreementSchema**](ContractAgreementSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract agreement |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract agreement with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiation_by_agreement_id_v5**
> ContractAgreementSchema get_negotiation_by_agreement_id_v5(participant_context_id, id)

Gets a contract negotiation with the given contract agreement ID

### Example


```python
import openapi_client
from openapi_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = openapi_client.ContractAgreementV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_by_agreement_id_v5(participant_context_id, id)
        print("The response of ContractAgreementV5betaApi->get_negotiation_by_agreement_id_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV5betaApi->get_negotiation_by_agreement_id_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ContractAgreementSchema**](ContractAgreementSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiation |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract agreement with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_agreements_v5**
> List[ContractAgreementSchema] query_agreements_v5(participant_context_id, query_spec_schema=query_spec_schema)

Gets all contract agreements according to a particular query

### Example


```python
import openapi_client
from openapi_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = openapi_client.ContractAgreementV5betaApi(api_client)
    participant_context_id = 'participant_context_id_example' # str | 
    query_spec_schema = openapi_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_agreements_v5(participant_context_id, query_spec_schema=query_spec_schema)
        print("The response of ContractAgreementV5betaApi->query_agreements_v5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV5betaApi->query_agreements_v5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_context_id** | **str**|  | 
 **query_spec_schema** | [**QuerySpecSchema**](QuerySpecSchema.md)|  | [optional] 

### Return type

[**List[ContractAgreementSchema]**](ContractAgreementSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract agreements matching the query |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

