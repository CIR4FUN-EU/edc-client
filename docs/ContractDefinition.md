# ContractDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**access_policy_id** | **str** |  | 
**contract_policy_id** | **str** |  | 
**private_properties** | **object** |  | [optional] 
**assets_selector** | [**List[Criterion]**](Criterion.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_definition import ContractDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinition from a JSON string
contract_definition_instance = ContractDefinition.from_json(json)
# print the JSON string representation of the object
print(ContractDefinition.to_json())

# convert the object into a dict
contract_definition_dict = contract_definition_instance.to_dict()
# create an instance of ContractDefinition from a dict
contract_definition_from_dict = ContractDefinition.from_dict(contract_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


