# ContractOffer


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
from edc_client.models.contract_offer import ContractOffer

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOffer from a JSON string
contract_offer_instance = ContractOffer.from_json(json)
# print the JSON string representation of the object
print(ContractOffer.to_json())

# convert the object into a dict
contract_offer_dict = contract_offer_instance.to_dict()
# create an instance of ContractOffer from a dict
contract_offer_from_dict = ContractOffer.from_dict(contract_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


