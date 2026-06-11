# TransferSuspendSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transfer_suspend_schema import TransferSuspendSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransferSuspendSchema from a JSON string
transfer_suspend_schema_instance = TransferSuspendSchema.from_json(json)
# print the JSON string representation of the object
print(TransferSuspendSchema.to_json())

# convert the object into a dict
transfer_suspend_schema_dict = transfer_suspend_schema_instance.to_dict()
# create an instance of TransferSuspendSchema from a dict
transfer_suspend_schema_from_dict = TransferSuspendSchema.from_dict(transfer_suspend_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


