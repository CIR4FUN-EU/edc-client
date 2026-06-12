# IdResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**created_at** | **float** |  | 

## Example

```python
from edc_client.models.id_response_schema import IdResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IdResponseSchema from a JSON string
id_response_schema_instance = IdResponseSchema.from_json(json)
# print the JSON string representation of the object
print(IdResponseSchema.to_json())

# convert the object into a dict
id_response_schema_dict = id_response_schema_instance.to_dict()
# create an instance of IdResponseSchema from a dict
id_response_schema_from_dict = IdResponseSchema.from_dict(id_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


