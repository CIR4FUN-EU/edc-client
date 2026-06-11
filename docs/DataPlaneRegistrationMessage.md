# DataPlaneRegistrationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **Dict[str, object]** |  | [optional] 
**dataplane_id** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**transfer_types** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.data_plane_registration_message import DataPlaneRegistrationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DataPlaneRegistrationMessage from a JSON string
data_plane_registration_message_instance = DataPlaneRegistrationMessage.from_json(json)
# print the JSON string representation of the object
print(DataPlaneRegistrationMessage.to_json())

# convert the object into a dict
data_plane_registration_message_dict = data_plane_registration_message_instance.to_dict()
# create an instance of DataPlaneRegistrationMessage from a dict
data_plane_registration_message_from_dict = DataPlaneRegistrationMessage.from_dict(data_plane_registration_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


