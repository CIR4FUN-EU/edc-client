# CelExpressionTestRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**expression** | **str** |  | 
**left_operand** | **str** |  | 
**operator** | **str** |  | 
**right_operand** | [**CelExpressionTestRequestRightOperand**](CelExpressionTestRequestRightOperand.md) |  | 
**params** | **object** |  | [optional] 

## Example

```python
from edc_client.models.cel_expression_test_request_schema import CelExpressionTestRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CelExpressionTestRequestSchema from a JSON string
cel_expression_test_request_schema_instance = CelExpressionTestRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CelExpressionTestRequestSchema.to_json())

# convert the object into a dict
cel_expression_test_request_schema_dict = cel_expression_test_request_schema_instance.to_dict()
# create an instance of CelExpressionTestRequestSchema from a dict
cel_expression_test_request_schema_from_dict = CelExpressionTestRequestSchema.from_dict(cel_expression_test_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


