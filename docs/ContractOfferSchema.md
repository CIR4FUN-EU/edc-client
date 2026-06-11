# ContractOfferSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**profile** | [**PolicyClassProfile**](PolicyClassProfile.md) |  | [optional] 
**permission** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibition** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**obligation** | [**List[Duty]**](Duty.md) |  | [optional] 
**type** | **str** |  | 
**target** | **str** |  | 
**assigner** | **str** |  | 

## Example

```python
from openapi_client.models.contract_offer_schema import ContractOfferSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOfferSchema from a JSON string
contract_offer_schema_instance = ContractOfferSchema.from_json(json)
# print the JSON string representation of the object
print(ContractOfferSchema.to_json())

# convert the object into a dict
contract_offer_schema_dict = contract_offer_schema_instance.to_dict()
# create an instance of ContractOfferSchema from a dict
contract_offer_schema_from_dict = ContractOfferSchema.from_dict(contract_offer_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


