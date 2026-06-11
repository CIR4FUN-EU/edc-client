# CelExpression


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
from openapi_client.models.cel_expression import CelExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CelExpression from a JSON string
cel_expression_instance = CelExpression.from_json(json)
# print the JSON string representation of the object
print(CelExpression.to_json())

# convert the object into a dict
cel_expression_dict = cel_expression_instance.to_dict()
# create an instance of CelExpression from a dict
cel_expression_from_dict = CelExpression.from_dict(cel_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


