# DutyStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | [optional] 
**rule_functions** | **List[str]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.duty_step import DutyStep

# TODO update the JSON string below
json = "{}"
# create an instance of DutyStep from a JSON string
duty_step_instance = DutyStep.from_json(json)
# print the JSON string representation of the object
print(DutyStep.to_json())

# convert the object into a dict
duty_step_dict = duty_step_instance.to_dict()
# create an instance of DutyStep from a dict
duty_step_from_dict = DutyStep.from_dict(duty_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


