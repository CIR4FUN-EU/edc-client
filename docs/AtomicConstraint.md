# AtomicConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**right_operand** | [**RightOperand**](RightOperand.md) |  | 
**left_operand** | **str** |  | 
**operator** | [**Operator**](Operator.md) |  | 

## Example

```python
from openapi_client.models.atomic_constraint import AtomicConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicConstraint from a JSON string
atomic_constraint_instance = AtomicConstraint.from_json(json)
# print the JSON string representation of the object
print(AtomicConstraint.to_json())

# convert the object into a dict
atomic_constraint_dict = atomic_constraint_instance.to_dict()
# create an instance of AtomicConstraint from a dict
atomic_constraint_from_dict = AtomicConstraint.from_dict(atomic_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


