# MessageOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**profile** | [**PolicyClassProfile**](PolicyClassProfile.md) |  | [optional] 
**permission** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibition** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**obligation** | [**List[Duty]**](Duty.md) |  | [optional] 
**type** | **str** |  | 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.message_offer import MessageOffer

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOffer from a JSON string
message_offer_instance = MessageOffer.from_json(json)
# print the JSON string representation of the object
print(MessageOffer.to_json())

# convert the object into a dict
message_offer_dict = message_offer_instance.to_dict()
# create an instance of MessageOffer from a dict
message_offer_from_dict = MessageOffer.from_dict(message_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


