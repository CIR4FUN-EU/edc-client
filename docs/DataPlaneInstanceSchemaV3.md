# DataPlaneInstanceSchemaV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**allowed_dest_types** | **List[str]** |  | 
**allowed_source_types** | **List[str]** |  | 
**last_active** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**state_timestamp** | **int** |  | [optional] 
**turn_count** | **int** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.data_plane_instance_schema_v3 import DataPlaneInstanceSchemaV3

# TODO update the JSON string below
json = "{}"
# create an instance of DataPlaneInstanceSchemaV3 from a JSON string
data_plane_instance_schema_v3_instance = DataPlaneInstanceSchemaV3.from_json(json)
# print the JSON string representation of the object
print(DataPlaneInstanceSchemaV3.to_json())

# convert the object into a dict
data_plane_instance_schema_v3_dict = data_plane_instance_schema_v3_instance.to_dict()
# create an instance of DataPlaneInstanceSchemaV3 from a dict
data_plane_instance_schema_v3_from_dict = DataPlaneInstanceSchemaV3.from_dict(data_plane_instance_schema_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


