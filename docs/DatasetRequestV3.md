# DatasetRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**counter_party_address** | **str** |  | [optional] 
**counter_party_id** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**query_spec** | [**QuerySpec5**](QuerySpec5.md) |  | [optional] 

## Example

```python
from openapi_client.models.dataset_request_v3 import DatasetRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetRequestV3 from a JSON string
dataset_request_v3_instance = DatasetRequestV3.from_json(json)
# print the JSON string representation of the object
print(DatasetRequestV3.to_json())

# convert the object into a dict
dataset_request_v3_dict = dataset_request_v3_instance.to_dict()
# create an instance of DatasetRequestV3 from a dict
dataset_request_v3_from_dict = DatasetRequestV3.from_dict(dataset_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


