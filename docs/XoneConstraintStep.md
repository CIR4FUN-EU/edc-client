# XoneConstraintStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | 
**type** | **str** |  | 

## Example

```python
from edc_client.models.xone_constraint_step import XoneConstraintStep

# TODO update the JSON string below
json = "{}"
# create an instance of XoneConstraintStep from a JSON string
xone_constraint_step_instance = XoneConstraintStep.from_json(json)
# print the JSON string representation of the object
print(XoneConstraintStep.to_json())

# convert the object into a dict
xone_constraint_step_dict = xone_constraint_step_instance.to_dict()
# create an instance of XoneConstraintStep from a dict
xone_constraint_step_from_dict = XoneConstraintStep.from_dict(xone_constraint_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


