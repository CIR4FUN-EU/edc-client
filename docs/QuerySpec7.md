# QuerySpec7


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
from edc_client.models.query_spec7 import QuerySpec7

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpec7 from a JSON string
query_spec7_instance = QuerySpec7.from_json(json)
# print the JSON string representation of the object
print(QuerySpec7.to_json())

# convert the object into a dict
query_spec7_dict = query_spec7_instance.to_dict()
# create an instance of QuerySpec7 from a dict
query_spec7_from_dict = QuerySpec7.from_dict(query_spec7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


