# QuerySpecRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**filter_expression** | [**List[Criterion]**](Criterion.md) |  | [optional] 
**context** | **List[str]** |  | 

## Example

```python
from openapi_client.models.query_spec_root import QuerySpecRoot

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpecRoot from a JSON string
query_spec_root_instance = QuerySpecRoot.from_json(json)
# print the JSON string representation of the object
print(QuerySpecRoot.to_json())

# convert the object into a dict
query_spec_root_dict = query_spec_root_instance.to_dict()
# create an instance of QuerySpecRoot from a dict
query_spec_root_from_dict = QuerySpecRoot.from_dict(query_spec_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


