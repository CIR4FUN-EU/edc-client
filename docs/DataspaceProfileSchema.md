# DataspaceProfileSchema


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
from edc_client.models.dataspace_profile_schema import DataspaceProfileSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataspaceProfileSchema from a JSON string
dataspace_profile_schema_instance = DataspaceProfileSchema.from_json(json)
# print the JSON string representation of the object
print(DataspaceProfileSchema.to_json())

# convert the object into a dict
dataspace_profile_schema_dict = dataspace_profile_schema_instance.to_dict()
# create an instance of DataspaceProfileSchema from a dict
dataspace_profile_schema_from_dict = DataspaceProfileSchema.from_dict(dataspace_profile_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


