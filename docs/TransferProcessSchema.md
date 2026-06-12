# TransferProcessSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**state** | **str** |  | 
**state_timestamp** | **int** |  | 
**callback_addresses** | [**List[CallbackAddressSchema]**](CallbackAddressSchema.md) |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**contract_id** | **str** |  | [optional] 
**transfer_type** | **str** |  | [optional] 
**error_detail** | **str** |  | [optional] 
**dataplane_metadata** | [**DataplaneMetadataSchema**](DataplaneMetadataSchema.md) |  | [optional] 

## Example

```python
from edc_client.models.transfer_process_schema import TransferProcessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransferProcessSchema from a JSON string
transfer_process_schema_instance = TransferProcessSchema.from_json(json)
# print the JSON string representation of the object
print(TransferProcessSchema.to_json())

# convert the object into a dict
transfer_process_schema_dict = transfer_process_schema_instance.to_dict()
# create an instance of TransferProcessSchema from a dict
transfer_process_schema_from_dict = TransferProcessSchema.from_dict(transfer_process_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


