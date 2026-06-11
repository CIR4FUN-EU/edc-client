# CelExpressionTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**evaluation_result** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cel_expression_test_response import CelExpressionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CelExpressionTestResponse from a JSON string
cel_expression_test_response_instance = CelExpressionTestResponse.from_json(json)
# print the JSON string representation of the object
print(CelExpressionTestResponse.to_json())

# convert the object into a dict
cel_expression_test_response_dict = cel_expression_test_response_instance.to_dict()
# create an instance of CelExpressionTestResponse from a dict
cel_expression_test_response_from_dict = CelExpressionTestResponse.from_dict(cel_expression_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


