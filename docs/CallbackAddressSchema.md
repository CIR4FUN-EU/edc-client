# CallbackAddressSchema


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
from edc_client.models.callback_address_schema import CallbackAddressSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackAddressSchema from a JSON string
callback_address_schema_instance = CallbackAddressSchema.from_json(json)
# print the JSON string representation of the object
print(CallbackAddressSchema.to_json())

# convert the object into a dict
callback_address_schema_dict = callback_address_schema_instance.to_dict()
# create an instance of CallbackAddressSchema from a dict
callback_address_schema_from_dict = CallbackAddressSchema.from_dict(callback_address_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


