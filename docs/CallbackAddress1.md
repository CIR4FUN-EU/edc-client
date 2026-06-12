# CallbackAddress1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**auth_code_id** | **str** |  | [optional] 
**auth_key** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**transactional** | **bool** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from edc_client.models.callback_address1 import CallbackAddress1

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackAddress1 from a JSON string
callback_address1_instance = CallbackAddress1.from_json(json)
# print the JSON string representation of the object
print(CallbackAddress1.to_json())

# convert the object into a dict
callback_address1_dict = callback_address1_instance.to_dict()
# create an instance of CallbackAddress1 from a dict
callback_address1_from_dict = CallbackAddress1.from_dict(callback_address1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


