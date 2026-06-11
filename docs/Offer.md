# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**profile** | [**PolicyClassProfile**](PolicyClassProfile.md) |  | [optional] 
**permission** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibition** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**obligation** | [**List[Duty]**](Duty.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


