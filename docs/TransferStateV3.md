# TransferStateV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from edc_client.models.transfer_state_v3 import TransferStateV3

# TODO update the JSON string below
json = "{}"
# create an instance of TransferStateV3 from a JSON string
transfer_state_v3_instance = TransferStateV3.from_json(json)
# print the JSON string representation of the object
print(TransferStateV3.to_json())

# convert the object into a dict
transfer_state_v3_dict = transfer_state_v3_instance.to_dict()
# create an instance of TransferStateV3 from a dict
transfer_state_v3_from_dict = TransferStateV3.from_dict(transfer_state_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


