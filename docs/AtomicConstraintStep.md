# AtomicConstraintStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**function_name** | **str** |  | [optional] 
**function_params** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.atomic_constraint_step import AtomicConstraintStep

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicConstraintStep from a JSON string
atomic_constraint_step_instance = AtomicConstraintStep.from_json(json)
# print the JSON string representation of the object
print(AtomicConstraintStep.to_json())

# convert the object into a dict
atomic_constraint_step_dict = atomic_constraint_step_instance.to_dict()
# create an instance of AtomicConstraintStep from a dict
atomic_constraint_step_from_dict = AtomicConstraintStep.from_dict(atomic_constraint_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


