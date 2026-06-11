# PolicyValidationResultSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**is_valid** | **bool** |  | 
**errors** | **List[str]** |  | 

## Example

```python
from openapi_client.models.policy_validation_result_schema import PolicyValidationResultSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyValidationResultSchema from a JSON string
policy_validation_result_schema_instance = PolicyValidationResultSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyValidationResultSchema.to_json())

# convert the object into a dict
policy_validation_result_schema_dict = policy_validation_result_schema_instance.to_dict()
# create an instance of PolicyValidationResultSchema from a dict
policy_validation_result_schema_from_dict = PolicyValidationResultSchema.from_dict(policy_validation_result_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


