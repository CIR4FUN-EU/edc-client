# CelExpressionTestRequest


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
from openapi_client.models.cel_expression_test_request import CelExpressionTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CelExpressionTestRequest from a JSON string
cel_expression_test_request_instance = CelExpressionTestRequest.from_json(json)
# print the JSON string representation of the object
print(CelExpressionTestRequest.to_json())

# convert the object into a dict
cel_expression_test_request_dict = cel_expression_test_request_instance.to_dict()
# create an instance of CelExpressionTestRequest from a dict
cel_expression_test_request_from_dict = CelExpressionTestRequest.from_dict(cel_expression_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


