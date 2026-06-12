# TransferState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**state** | **str** |  | 

## Example

```python
from edc_client.models.transfer_state import TransferState

# TODO update the JSON string below
json = "{}"
# create an instance of TransferState from a JSON string
transfer_state_instance = TransferState.from_json(json)
# print the JSON string representation of the object
print(TransferState.to_json())

# convert the object into a dict
transfer_state_dict = transfer_state_instance.to_dict()
# create an instance of TransferState from a dict
transfer_state_from_dict = TransferState.from_dict(transfer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


