# CallbackAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**transactional** | **bool** |  | 
**uri** | **str** |  | 
**events** | **List[str]** |  | 
**auth_key** | **str** |  | [optional] 
**auth_code_id** | **str** |  | [optional] 

## Example

```python
from edc_client.models.callback_address import CallbackAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackAddress from a JSON string
callback_address_instance = CallbackAddress.from_json(json)
# print the JSON string representation of the object
print(CallbackAddress.to_json())

# convert the object into a dict
callback_address_dict = callback_address_instance.to_dict()
# create an instance of CallbackAddress from a dict
callback_address_from_dict = CallbackAddress.from_dict(callback_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


