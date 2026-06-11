# TransferProcessV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddress1]**](CallbackAddress1.md) |  | [optional] 
**contract_agreement_id** | **str** |  | [optional] 
**counter_party_address** | **str** |  | [optional] 
**counter_party_id** | **str** |  | [optional] 
**data_destination** | [**DataAddress**](DataAddress.md) |  | [optional] 
**error_detail** | **str** |  | [optional] 
**private_properties** | **Dict[str, object]** |  | [optional] 
**protocol** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transfer_process_v3 import TransferProcessV3

# TODO update the JSON string below
json = "{}"
# create an instance of TransferProcessV3 from a JSON string
transfer_process_v3_instance = TransferProcessV3.from_json(json)
# print the JSON string representation of the object
print(TransferProcessV3.to_json())

# convert the object into a dict
transfer_process_v3_dict = transfer_process_v3_instance.to_dict()
# create an instance of TransferProcessV3 from a dict
transfer_process_v3_from_dict = TransferProcessV3.from_dict(transfer_process_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


