# DataspaceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**protocol** | [**DataspaceProfileProtocol**](DataspaceProfileProtocol.md) |  | 
**json_ld_contexts_url** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.dataspace_profile import DataspaceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DataspaceProfile from a JSON string
dataspace_profile_instance = DataspaceProfile.from_json(json)
# print the JSON string representation of the object
print(DataspaceProfile.to_json())

# convert the object into a dict
dataspace_profile_dict = dataspace_profile_instance.to_dict()
# create an instance of DataspaceProfile from a dict
dataspace_profile_from_dict = DataspaceProfile.from_dict(dataspace_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


