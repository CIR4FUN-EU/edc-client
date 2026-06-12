# RootCatalog


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
from edc_client.models.root_catalog import RootCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of RootCatalog from a JSON string
root_catalog_instance = RootCatalog.from_json(json)
# print the JSON string representation of the object
print(RootCatalog.to_json())

# convert the object into a dict
root_catalog_dict = root_catalog_instance.to_dict()
# create an instance of RootCatalog from a dict
root_catalog_from_dict = RootCatalog.from_dict(root_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


