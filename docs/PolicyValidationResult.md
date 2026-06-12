# PolicyValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**is_valid** | **bool** |  | 
**errors** | **List[str]** |  | 

## Example

```python
from edc_client.models.policy_validation_result import PolicyValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyValidationResult from a JSON string
policy_validation_result_instance = PolicyValidationResult.from_json(json)
# print the JSON string representation of the object
print(PolicyValidationResult.to_json())

# convert the object into a dict
policy_validation_result_dict = policy_validation_result_instance.to_dict()
# create an instance of PolicyValidationResult from a dict
policy_validation_result_from_dict = PolicyValidationResult.from_dict(policy_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


