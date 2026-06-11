# ContractAgreement


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
from openapi_client.models.contract_agreement import ContractAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAgreement from a JSON string
contract_agreement_instance = ContractAgreement.from_json(json)
# print the JSON string representation of the object
print(ContractAgreement.to_json())

# convert the object into a dict
contract_agreement_dict = contract_agreement_instance.to_dict()
# create an instance of ContractAgreement from a dict
contract_agreement_from_dict = ContractAgreement.from_dict(contract_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


