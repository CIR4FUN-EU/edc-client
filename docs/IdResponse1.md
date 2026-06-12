# IdResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from edc_client.models.id_response1 import IdResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of IdResponse1 from a JSON string
id_response1_instance = IdResponse1.from_json(json)
# print the JSON string representation of the object
print(IdResponse1.to_json())

# convert the object into a dict
id_response1_dict = id_response1_instance.to_dict()
# create an instance of IdResponse1 from a dict
id_response1_from_dict = IdResponse1.from_dict(id_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


