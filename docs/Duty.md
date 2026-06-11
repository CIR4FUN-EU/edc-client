# Duty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**constraint** | [**List[Constraint]**](Constraint.md) |  | [optional] 

## Example

```python
from openapi_client.models.duty import Duty

# TODO update the JSON string below
json = "{}"
# create an instance of Duty from a JSON string
duty_instance = Duty.from_json(json)
# print the JSON string representation of the object
print(Duty.to_json())

# convert the object into a dict
duty_dict = duty_instance.to_dict()
# create an instance of Duty from a dict
duty_from_dict = Duty.from_dict(duty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


