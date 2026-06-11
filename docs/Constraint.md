# Constraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**and_sequence** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**var_or** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**xone** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**right_operand** | [**RightOperand**](RightOperand.md) |  | 
**left_operand** | **str** |  | 
**operator** | [**Operator**](Operator.md) |  | 

## Example

```python
from openapi_client.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print(Constraint.to_json())

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_from_dict = Constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


