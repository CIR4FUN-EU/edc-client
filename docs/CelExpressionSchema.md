# CelExpressionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**left_operand** | **str** |  | 
**expression** | **str** |  | 
**description** | **str** |  | 
**scopes** | **List[str]** |  | [optional] 
**actions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.cel_expression_schema import CelExpressionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CelExpressionSchema from a JSON string
cel_expression_schema_instance = CelExpressionSchema.from_json(json)
# print the JSON string representation of the object
print(CelExpressionSchema.to_json())

# convert the object into a dict
cel_expression_schema_dict = cel_expression_schema_instance.to_dict()
# create an instance of CelExpressionSchema from a dict
cel_expression_schema_from_dict = CelExpressionSchema.from_dict(cel_expression_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


