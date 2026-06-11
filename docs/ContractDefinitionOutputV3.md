# ContractDefinitionOutputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**access_policy_id** | **str** |  | [optional] 
**assets_selector** | [**List[Criterion1]**](Criterion1.md) |  | [optional] 
**contract_policy_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.contract_definition_output_v3 import ContractDefinitionOutputV3

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinitionOutputV3 from a JSON string
contract_definition_output_v3_instance = ContractDefinitionOutputV3.from_json(json)
# print the JSON string representation of the object
print(ContractDefinitionOutputV3.to_json())

# convert the object into a dict
contract_definition_output_v3_dict = contract_definition_output_v3_instance.to_dict()
# create an instance of ContractDefinitionOutputV3 from a dict
contract_definition_output_v3_from_dict = ContractDefinitionOutputV3.from_dict(contract_definition_output_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


