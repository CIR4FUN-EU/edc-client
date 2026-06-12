# ContractDefinitionSchema


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
from edc_client.models.contract_definition_schema import ContractDefinitionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinitionSchema from a JSON string
contract_definition_schema_instance = ContractDefinitionSchema.from_json(json)
# print the JSON string representation of the object
print(ContractDefinitionSchema.to_json())

# convert the object into a dict
contract_definition_schema_dict = contract_definition_schema_instance.to_dict()
# create an instance of ContractDefinitionSchema from a dict
contract_definition_schema_from_dict = ContractDefinitionSchema.from_dict(contract_definition_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


