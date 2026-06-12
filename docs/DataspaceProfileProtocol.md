# DataspaceProfileProtocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**path** | **str** |  | 
**binding** | **str** |  | 
**namespace** | **str** |  | 

## Example

```python
from edc_client.models.dataspace_profile_protocol import DataspaceProfileProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of DataspaceProfileProtocol from a JSON string
dataspace_profile_protocol_instance = DataspaceProfileProtocol.from_json(json)
# print the JSON string representation of the object
print(DataspaceProfileProtocol.to_json())

# convert the object into a dict
dataspace_profile_protocol_dict = dataspace_profile_protocol_instance.to_dict()
# create an instance of DataspaceProfileProtocol from a dict
dataspace_profile_protocol_from_dict = DataspaceProfileProtocol.from_dict(dataspace_profile_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


