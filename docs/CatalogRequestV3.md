# CatalogRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**type** | **str** |  | [optional] 
**additional_scopes** | **List[str]** |  | [optional] 
**counter_party_address** | **str** |  | 
**counter_party_id** | **str** |  | [optional] 
**protocol** | **str** |  | 
**query_spec** | [**QuerySpec5**](QuerySpec5.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_request_v3 import CatalogRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogRequestV3 from a JSON string
catalog_request_v3_instance = CatalogRequestV3.from_json(json)
# print the JSON string representation of the object
print(CatalogRequestV3.to_json())

# convert the object into a dict
catalog_request_v3_dict = catalog_request_v3_instance.to_dict()
# create an instance of CatalogRequestV3 from a dict
catalog_request_v3_from_dict = CatalogRequestV3.from_dict(catalog_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


