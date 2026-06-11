# QuerySpecSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**filter_expression** | [**List[Criterion]**](Criterion.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_spec_schema import QuerySpecSchema

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpecSchema from a JSON string
query_spec_schema_instance = QuerySpecSchema.from_json(json)
# print the JSON string representation of the object
print(QuerySpecSchema.to_json())

# convert the object into a dict
query_spec_schema_dict = query_spec_schema_instance.to_dict()
# create an instance of QuerySpecSchema from a dict
query_spec_schema_from_dict = QuerySpecSchema.from_dict(query_spec_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


