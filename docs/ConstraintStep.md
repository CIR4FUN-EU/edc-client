# ConstraintStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | 
**type** | **str** |  | 
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**function_name** | **str** |  | [optional] 
**function_params** | **List[str]** |  | [optional] 

## Example

```python
from edc_client.models.constraint_step import ConstraintStep

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintStep from a JSON string
constraint_step_instance = ConstraintStep.from_json(json)
# print the JSON string representation of the object
print(ConstraintStep.to_json())

# convert the object into a dict
constraint_step_dict = constraint_step_instance.to_dict()
# create an instance of ConstraintStep from a dict
constraint_step_from_dict = ConstraintStep.from_dict(constraint_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


