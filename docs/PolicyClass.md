# PolicyClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**profile** | [**PolicyClassProfile**](PolicyClassProfile.md) |  | [optional] 
**permission** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibition** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**obligation** | [**List[Duty]**](Duty.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_class import PolicyClass

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyClass from a JSON string
policy_class_instance = PolicyClass.from_json(json)
# print the JSON string representation of the object
print(PolicyClass.to_json())

# convert the object into a dict
policy_class_dict = policy_class_instance.to_dict()
# create an instance of PolicyClass from a dict
policy_class_from_dict = PolicyClass.from_dict(policy_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


