# ContractNegotiation1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**state** | **str** |  | 
**state_timestamp** | **int** |  | [optional] 
**protocol** | **str** |  | 
**profile** | **str** |  | 
**created_at** | **int** |  | 
**callback_addresses** | [**List[CallbackAddressSchema]**](CallbackAddressSchema.md) |  | [optional] 
**counter_party_address** | **str** |  | 
**counter_party_id** | **str** |  | 
**error_detail** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**contract_agreement_id** | **str** |  | [optional] 

## Example

```python
from edc_client.models.contract_negotiation1 import ContractNegotiation1

# TODO update the JSON string below
json = "{}"
# create an instance of ContractNegotiation1 from a JSON string
contract_negotiation1_instance = ContractNegotiation1.from_json(json)
# print the JSON string representation of the object
print(ContractNegotiation1.to_json())

# convert the object into a dict
contract_negotiation1_dict = contract_negotiation1_instance.to_dict()
# create an instance of ContractNegotiation1 from a dict
contract_negotiation1_from_dict = ContractNegotiation1.from_dict(contract_negotiation1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


