# PolicyDefinitionOutputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**policy** | **object** | ODRL policy | [optional] 

## Example

```python
from openapi_client.models.policy_definition_output_v3 import PolicyDefinitionOutputV3

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefinitionOutputV3 from a JSON string
policy_definition_output_v3_instance = PolicyDefinitionOutputV3.from_json(json)
# print the JSON string representation of the object
print(PolicyDefinitionOutputV3.to_json())

# convert the object into a dict
policy_definition_output_v3_dict = policy_definition_output_v3_instance.to_dict()
# create an instance of PolicyDefinitionOutputV3 from a dict
policy_definition_output_v3_from_dict = PolicyDefinitionOutputV3.from_dict(policy_definition_output_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


