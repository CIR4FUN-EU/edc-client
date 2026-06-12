# TerminateTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from edc_client.models.terminate_transfer import TerminateTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateTransfer from a JSON string
terminate_transfer_instance = TerminateTransfer.from_json(json)
# print the JSON string representation of the object
print(TerminateTransfer.to_json())

# convert the object into a dict
terminate_transfer_dict = terminate_transfer_instance.to_dict()
# create an instance of TerminateTransfer from a dict
terminate_transfer_from_dict = TerminateTransfer.from_dict(terminate_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


