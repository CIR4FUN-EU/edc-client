# ContractTerminateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contract_terminate_schema import ContractTerminateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractTerminateSchema from a JSON string
contract_terminate_schema_instance = ContractTerminateSchema.from_json(json)
# print the JSON string representation of the object
print(ContractTerminateSchema.to_json())

# convert the object into a dict
contract_terminate_schema_dict = contract_terminate_schema_instance.to_dict()
# create an instance of ContractTerminateSchema from a dict
contract_terminate_schema_from_dict = ContractTerminateSchema.from_dict(contract_terminate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


