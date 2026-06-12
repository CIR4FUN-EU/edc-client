# PolicyDefinitionInputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**policy** | **object** | ODRL policy | 

## Example

```python
from edc_client.models.policy_definition_input_v3 import PolicyDefinitionInputV3

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefinitionInputV3 from a JSON string
policy_definition_input_v3_instance = PolicyDefinitionInputV3.from_json(json)
# print the JSON string representation of the object
print(PolicyDefinitionInputV3.to_json())

# convert the object into a dict
policy_definition_input_v3_dict = policy_definition_input_v3_instance.to_dict()
# create an instance of PolicyDefinitionInputV3 from a dict
policy_definition_input_v3_from_dict = PolicyDefinitionInputV3.from_dict(policy_definition_input_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


