# QuerySpec8


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
from openapi_client.models.query_spec8 import QuerySpec8

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpec8 from a JSON string
query_spec8_instance = QuerySpec8.from_json(json)
# print the JSON string representation of the object
print(QuerySpec8.to_json())

# convert the object into a dict
query_spec8_dict = query_spec8_instance.to_dict()
# create an instance of QuerySpec8 from a dict
query_spec8_from_dict = QuerySpec8.from_dict(query_spec8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


