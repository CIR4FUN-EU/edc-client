# TransferRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**type** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddress1]**](CallbackAddress1.md) |  | [optional] 
**contract_id** | **str** |  | 
**counter_party_address** | **str** |  | 
**data_destination** | [**DataAddress**](DataAddress.md) |  | [optional] 
**private_properties** | **Dict[str, object]** |  | [optional] 
**protocol** | **str** |  | 
**transfer_type** | **str** |  | 

## Example

```python
from openapi_client.models.transfer_request_v3 import TransferRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequestV3 from a JSON string
transfer_request_v3_instance = TransferRequestV3.from_json(json)
# print the JSON string representation of the object
print(TransferRequestV3.to_json())

# convert the object into a dict
transfer_request_v3_dict = transfer_request_v3_instance.to_dict()
# create an instance of TransferRequestV3 from a dict
transfer_request_v3_from_dict = TransferRequestV3.from_dict(transfer_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


