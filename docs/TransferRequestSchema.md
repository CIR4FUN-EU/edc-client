# TransferRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**counter_party_address** | **str** |  | 
**protocol** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**contract_id** | **str** |  | 
**transfer_type** | **str** |  | 
**private_properties** | **object** |  | [optional] 
**callback_addresses** | [**List[CallbackAddressSchema]**](CallbackAddressSchema.md) |  | [optional] 
**dataplane_metadata** | [**DataplaneMetadataSchema**](DataplaneMetadataSchema.md) |  | [optional] 

## Example

```python
from edc_client.models.transfer_request_schema import TransferRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequestSchema from a JSON string
transfer_request_schema_instance = TransferRequestSchema.from_json(json)
# print the JSON string representation of the object
print(TransferRequestSchema.to_json())

# convert the object into a dict
transfer_request_schema_dict = transfer_request_schema_instance.to_dict()
# create an instance of TransferRequestSchema from a dict
transfer_request_schema_from_dict = TransferRequestSchema.from_dict(transfer_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


