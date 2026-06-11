# PermissionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | [optional] 
**rule_functions** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**duty_steps** | [**List[DutyStep]**](DutyStep.md) |  | [optional] 

## Example

```python
from openapi_client.models.permission_step import PermissionStep

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionStep from a JSON string
permission_step_instance = PermissionStep.from_json(json)
# print the JSON string representation of the object
print(PermissionStep.to_json())

# convert the object into a dict
permission_step_dict = permission_step_instance.to_dict()
# create an instance of PermissionStep from a dict
permission_step_from_dict = PermissionStep.from_dict(permission_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


