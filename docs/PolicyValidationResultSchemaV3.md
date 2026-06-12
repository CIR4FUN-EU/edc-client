# PolicyValidationResultSchemaV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**is_valid** | **bool** |  | [optional] 

## Example

```python
from edc_client.models.policy_validation_result_schema_v3 import PolicyValidationResultSchemaV3

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyValidationResultSchemaV3 from a JSON string
policy_validation_result_schema_v3_instance = PolicyValidationResultSchemaV3.from_json(json)
# print the JSON string representation of the object
print(PolicyValidationResultSchemaV3.to_json())

# convert the object into a dict
policy_validation_result_schema_v3_dict = policy_validation_result_schema_v3_instance.to_dict()
# create an instance of PolicyValidationResultSchemaV3 from a dict
policy_validation_result_schema_v3_from_dict = PolicyValidationResultSchemaV3.from_dict(policy_validation_result_schema_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


