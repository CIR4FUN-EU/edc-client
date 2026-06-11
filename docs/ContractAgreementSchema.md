# ContractAgreementSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**asset_id** | **str** |  | 
**provider_id** | **str** |  | 
**consumer_id** | **str** |  | 
**contract_signing_date** | **int** |  | 
**policy** | [**Agreement**](Agreement.md) |  | 

## Example

```python
from openapi_client.models.contract_agreement_schema import ContractAgreementSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAgreementSchema from a JSON string
contract_agreement_schema_instance = ContractAgreementSchema.from_json(json)
# print the JSON string representation of the object
print(ContractAgreementSchema.to_json())

# convert the object into a dict
contract_agreement_schema_dict = contract_agreement_schema_instance.to_dict()
# create an instance of ContractAgreementSchema from a dict
contract_agreement_schema_from_dict = ContractAgreementSchema.from_dict(contract_agreement_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


