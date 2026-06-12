# LogicalConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**and_sequence** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**var_or** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**xone** | [**List[Constraint]**](Constraint.md) |  | [optional] 

## Example

```python
from edc_client.models.logical_constraint import LogicalConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalConstraint from a JSON string
logical_constraint_instance = LogicalConstraint.from_json(json)
# print the JSON string representation of the object
print(LogicalConstraint.to_json())

# convert the object into a dict
logical_constraint_dict = logical_constraint_instance.to_dict()
# create an instance of LogicalConstraint from a dict
logical_constraint_from_dict = LogicalConstraint.from_dict(logical_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


