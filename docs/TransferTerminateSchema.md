# TransferTerminateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from edc_client.models.transfer_terminate_schema import TransferTerminateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTerminateSchema from a JSON string
transfer_terminate_schema_instance = TransferTerminateSchema.from_json(json)
# print the JSON string representation of the object
print(TransferTerminateSchema.to_json())

# convert the object into a dict
transfer_terminate_schema_dict = transfer_terminate_schema_instance.to_dict()
# create an instance of TransferTerminateSchema from a dict
transfer_terminate_schema_from_dict = TransferTerminateSchema.from_dict(transfer_terminate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


