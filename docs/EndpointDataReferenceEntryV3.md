# EndpointDataReferenceEntryV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from edc_client.models.endpoint_data_reference_entry_v3 import EndpointDataReferenceEntryV3

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDataReferenceEntryV3 from a JSON string
endpoint_data_reference_entry_v3_instance = EndpointDataReferenceEntryV3.from_json(json)
# print the JSON string representation of the object
print(EndpointDataReferenceEntryV3.to_json())

# convert the object into a dict
endpoint_data_reference_entry_v3_dict = endpoint_data_reference_entry_v3_instance.to_dict()
# create an instance of EndpointDataReferenceEntryV3 from a dict
endpoint_data_reference_entry_v3_from_dict = EndpointDataReferenceEntryV3.from_dict(endpoint_data_reference_entry_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


