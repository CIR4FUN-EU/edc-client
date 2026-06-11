# ContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**counter_party_address** | **str** |  | 
**protocol** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**policy** | [**ContractOfferSchema**](ContractOfferSchema.md) |  | 
**callback_addresses** | [**List[CallbackAddressSchema]**](CallbackAddressSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_request import ContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContractRequest from a JSON string
contract_request_instance = ContractRequest.from_json(json)
# print the JSON string representation of the object
print(ContractRequest.to_json())

# convert the object into a dict
contract_request_dict = contract_request_instance.to_dict()
# create an instance of ContractRequest from a dict
contract_request_from_dict = ContractRequest.from_dict(contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


