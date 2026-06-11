# PolicyDefinitionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**policy** | [**PolicyClass**](PolicyClass.md) |  | 
**private_properties** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.policy_definition_schema import PolicyDefinitionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefinitionSchema from a JSON string
policy_definition_schema_instance = PolicyDefinitionSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyDefinitionSchema.to_json())

# convert the object into a dict
policy_definition_schema_dict = policy_definition_schema_instance.to_dict()
# create an instance of PolicyDefinitionSchema from a dict
policy_definition_schema_from_dict = PolicyDefinitionSchema.from_dict(policy_definition_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


