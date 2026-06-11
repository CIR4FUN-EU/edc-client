# ContractRequestSchema


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
from openapi_client.models.contract_request_schema import ContractRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractRequestSchema from a JSON string
contract_request_schema_instance = ContractRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ContractRequestSchema.to_json())

# convert the object into a dict
contract_request_schema_dict = contract_request_schema_instance.to_dict()
# create an instance of ContractRequestSchema from a dict
contract_request_schema_from_dict = ContractRequestSchema.from_dict(contract_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


