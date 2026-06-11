# DataplaneMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**labels** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**profiles** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.dataplane_metadata import DataplaneMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DataplaneMetadata from a JSON string
dataplane_metadata_instance = DataplaneMetadata.from_json(json)
# print the JSON string representation of the object
print(DataplaneMetadata.to_json())

# convert the object into a dict
dataplane_metadata_dict = dataplane_metadata_instance.to_dict()
# create an instance of DataplaneMetadata from a dict
dataplane_metadata_from_dict = DataplaneMetadata.from_dict(dataplane_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


