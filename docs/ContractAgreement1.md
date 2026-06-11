# ContractAgreement1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**consumer_id** | **str** |  | [optional] 
**contract_signing_date** | **int** |  | [optional] 
**policy** | **object** | ODRL policy | [optional] 
**provider_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contract_agreement1 import ContractAgreement1

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAgreement1 from a JSON string
contract_agreement1_instance = ContractAgreement1.from_json(json)
# print the JSON string representation of the object
print(ContractAgreement1.to_json())

# convert the object into a dict
contract_agreement1_dict = contract_agreement1_instance.to_dict()
# create an instance of ContractAgreement1 from a dict
contract_agreement1_from_dict = ContractAgreement1.from_dict(contract_agreement1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


