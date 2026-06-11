# SuspendTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.suspend_transfer import SuspendTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendTransfer from a JSON string
suspend_transfer_instance = SuspendTransfer.from_json(json)
# print the JSON string representation of the object
print(SuspendTransfer.to_json())

# convert the object into a dict
suspend_transfer_dict = suspend_transfer_instance.to_dict()
# create an instance of SuspendTransfer from a dict
suspend_transfer_from_dict = SuspendTransfer.from_dict(suspend_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


