# OfferV3

ODRL offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**assigner** | **str** |  | 
**target** | **str** |  | 

## Example

```python
from edc_client.models.offer_v3 import OfferV3

# TODO update the JSON string below
json = "{}"
# create an instance of OfferV3 from a JSON string
offer_v3_instance = OfferV3.from_json(json)
# print the JSON string representation of the object
print(OfferV3.to_json())

# convert the object into a dict
offer_v3_dict = offer_v3_instance.to_dict()
# create an instance of OfferV3 from a dict
offer_v3_from_dict = OfferV3.from_dict(offer_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


