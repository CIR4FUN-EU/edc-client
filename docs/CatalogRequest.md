# CatalogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**counter_party_address** | **str** |  | 
**counter_party_id** | **str** |  | 
**additional_scopes** | **List[str]** |  | [optional] 
**query_spec** | [**QuerySpec**](QuerySpec.md) |  | [optional] 

## Example

```python
from edc_client.models.catalog_request import CatalogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogRequest from a JSON string
catalog_request_instance = CatalogRequest.from_json(json)
# print the JSON string representation of the object
print(CatalogRequest.to_json())

# convert the object into a dict
catalog_request_dict = catalog_request_instance.to_dict()
# create an instance of CatalogRequest from a dict
catalog_request_from_dict = CatalogRequest.from_dict(catalog_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


