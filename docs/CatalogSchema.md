# CatalogSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**distribution** | [**List[Distribution]**](Distribution.md) |  | [optional] 
**type** | **str** |  | 
**dataset** | [**List[Dataset]**](Dataset.md) |  | [optional] 
**catalog** | [**List[Catalog]**](Catalog.md) |  | [optional] 
**service** | [**List[DataService]**](DataService.md) |  | [optional] 
**context** | **List[str]** |  | 
**participant_id** | **str** |  | 

## Example

```python
from openapi_client.models.catalog_schema import CatalogSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogSchema from a JSON string
catalog_schema_instance = CatalogSchema.from_json(json)
# print the JSON string representation of the object
print(CatalogSchema.to_json())

# convert the object into a dict
catalog_schema_dict = catalog_schema_instance.to_dict()
# create an instance of CatalogSchema from a dict
catalog_schema_from_dict = CatalogSchema.from_dict(catalog_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


