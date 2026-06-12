# DataPlaneInstanceSchemaV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**allowed_source_types** | **List[str]** |  | 
**last_active** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**state_timestamp** | **int** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from edc_client.models.data_plane_instance_schema_v4 import DataPlaneInstanceSchemaV4

# TODO update the JSON string below
json = "{}"
# create an instance of DataPlaneInstanceSchemaV4 from a JSON string
data_plane_instance_schema_v4_instance = DataPlaneInstanceSchemaV4.from_json(json)
# print the JSON string representation of the object
print(DataPlaneInstanceSchemaV4.to_json())

# convert the object into a dict
data_plane_instance_schema_v4_dict = data_plane_instance_schema_v4_instance.to_dict()
# create an instance of DataPlaneInstanceSchemaV4 from a dict
data_plane_instance_schema_v4_from_dict = DataPlaneInstanceSchemaV4.from_dict(data_plane_instance_schema_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


