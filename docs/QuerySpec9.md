# QuerySpec9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**filter_expression** | [**List[Criterion1]**](Criterion1.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.query_spec9 import QuerySpec9

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpec9 from a JSON string
query_spec9_instance = QuerySpec9.from_json(json)
# print the JSON string representation of the object
print(QuerySpec9.to_json())

# convert the object into a dict
query_spec9_dict = query_spec9_instance.to_dict()
# create an instance of QuerySpec9 from a dict
query_spec9_from_dict = QuerySpec9.from_dict(query_spec9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


