# edc_client.ContractAgreementV4Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agreement_by_id_v4**](ContractAgreementV4Api.md#get_agreement_by_id_v4) | **GET** /v4/contractagreements/{id} | 
[**get_negotiation_by_agreement_id_v4**](ContractAgreementV4Api.md#get_negotiation_by_agreement_id_v4) | **GET** /v4/contractagreements/{id}/negotiation | 
[**query_agreements_v4**](ContractAgreementV4Api.md#query_agreements_v4) | **POST** /v4/contractagreements/request | 


# **get_agreement_by_id_v4**
> ContractAgreementSchema get_agreement_by_id_v4(id)

Gets an contract agreement with the given ID

### Example


```python
import edc_client
from edc_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = edc_client.ContractAgreementV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_by_id_v4(id)
        print("The response of ContractAgreementV4Api->get_agreement_by_id_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV4Api->get_agreement_by_id_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_negotiation_by_agreement_id_v4**
> ContractAgreementSchema get_negotiation_by_agreement_id_v4(id)

Gets a contract negotiation with the given contract agreement ID

### Example


```python
import edc_client
from edc_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = edc_client.ContractAgreementV4Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_by_agreement_id_v4(id)
        print("The response of ContractAgreementV4Api->get_negotiation_by_agreement_id_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV4Api->get_negotiation_by_agreement_id_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **query_agreements_v4**
> List[ContractAgreementSchema] query_agreements_v4(query_spec_schema=query_spec_schema)

Gets all contract agreements according to a particular query

### Example


```python
import edc_client
from edc_client.models.contract_agreement_schema import ContractAgreementSchema
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
    api_instance = edc_client.ContractAgreementV4Api(api_client)
    query_spec_schema = edc_client.QuerySpecSchema() # QuerySpecSchema |  (optional)

    try:
        api_response = api_instance.query_agreements_v4(query_spec_schema=query_spec_schema)
        print("The response of ContractAgreementV4Api->query_agreements_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementV4Api->query_agreements_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

