# UpdateExpressionV5Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 
**value_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_expression_v5_request import UpdateExpressionV5Request

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExpressionV5Request from a JSON string
update_expression_v5_request_instance = UpdateExpressionV5Request.from_json(json)
# print the JSON string representation of the object
print(UpdateExpressionV5Request.to_json())

# convert the object into a dict
update_expression_v5_request_dict = update_expression_v5_request_instance.to_dict()
# create an instance of UpdateExpressionV5Request from a dict
update_expression_v5_request_from_dict = UpdateExpressionV5Request.from_dict(update_expression_v5_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


