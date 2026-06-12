# DataplaneMetadataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**labels** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**profiles** | **List[str]** |  | [optional] 

## Example

```python
from edc_client.models.dataplane_metadata_schema import DataplaneMetadataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataplaneMetadataSchema from a JSON string
dataplane_metadata_schema_instance = DataplaneMetadataSchema.from_json(json)
# print the JSON string representation of the object
print(DataplaneMetadataSchema.to_json())

# convert the object into a dict
dataplane_metadata_schema_dict = dataplane_metadata_schema_instance.to_dict()
# create an instance of DataplaneMetadataSchema from a dict
dataplane_metadata_schema_from_dict = DataplaneMetadataSchema.from_dict(dataplane_metadata_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


