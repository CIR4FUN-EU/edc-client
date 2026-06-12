# ContractAgreement2


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
from edc_client.models.contract_agreement2 import ContractAgreement2

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAgreement2 from a JSON string
contract_agreement2_instance = ContractAgreement2.from_json(json)
# print the JSON string representation of the object
print(ContractAgreement2.to_json())

# convert the object into a dict
contract_agreement2_dict = contract_agreement2_instance.to_dict()
# create an instance of ContractAgreement2 from a dict
contract_agreement2_from_dict = ContractAgreement2.from_dict(contract_agreement2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


