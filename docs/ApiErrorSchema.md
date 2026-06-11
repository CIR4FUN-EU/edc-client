# ApiErrorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**type** | **str** |  | 
**path** | **str** |  | [optional] 
**invalid_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_error_schema import ApiErrorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorSchema from a JSON string
api_error_schema_instance = ApiErrorSchema.from_json(json)
# print the JSON string representation of the object
print(ApiErrorSchema.to_json())

# convert the object into a dict
api_error_schema_dict = api_error_schema_instance.to_dict()
# create an instance of ApiErrorSchema from a dict
api_error_schema_from_dict = ApiErrorSchema.from_dict(api_error_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


