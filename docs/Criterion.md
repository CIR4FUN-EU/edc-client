# Criterion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**operand_left** | **str** |  | 
**operand_right** | **object** |  | 
**operator** | **str** |  | 

## Example

```python
from openapi_client.models.criterion import Criterion

# TODO update the JSON string below
json = "{}"
# create an instance of Criterion from a JSON string
criterion_instance = Criterion.from_json(json)
# print the JSON string representation of the object
print(Criterion.to_json())

# convert the object into a dict
criterion_dict = criterion_instance.to_dict()
# create an instance of Criterion from a dict
criterion_from_dict = Criterion.from_dict(criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


