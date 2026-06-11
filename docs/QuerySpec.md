# QuerySpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**filter_expression** | [**List[Criterion]**](Criterion.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_spec import QuerySpec

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpec from a JSON string
query_spec_instance = QuerySpec.from_json(json)
# print the JSON string representation of the object
print(QuerySpec.to_json())

# convert the object into a dict
query_spec_dict = query_spec_instance.to_dict()
# create an instance of QuerySpec from a dict
query_spec_from_dict = QuerySpec.from_dict(query_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


