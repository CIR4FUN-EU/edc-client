# ContractDefinitionInputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**access_policy_id** | **str** |  | 
**assets_selector** | [**List[Criterion1]**](Criterion1.md) |  | 
**contract_policy_id** | **str** |  | 

## Example

```python
from edc_client.models.contract_definition_input_v3 import ContractDefinitionInputV3

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinitionInputV3 from a JSON string
contract_definition_input_v3_instance = ContractDefinitionInputV3.from_json(json)
# print the JSON string representation of the object
print(ContractDefinitionInputV3.to_json())

# convert the object into a dict
contract_definition_input_v3_dict = contract_definition_input_v3_instance.to_dict()
# create an instance of ContractDefinitionInputV3 from a dict
contract_definition_input_v3_from_dict = ContractDefinitionInputV3.from_dict(contract_definition_input_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


