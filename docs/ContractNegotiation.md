# ContractNegotiation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddress1]**](CallbackAddress1.md) |  | [optional] 
**contract_agreement_id** | **str** |  | [optional] 
**counter_party_address** | **str** |  | [optional] 
**counter_party_id** | **str** |  | [optional] 
**error_detail** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contract_negotiation import ContractNegotiation

# TODO update the JSON string below
json = "{}"
# create an instance of ContractNegotiation from a JSON string
contract_negotiation_instance = ContractNegotiation.from_json(json)
# print the JSON string representation of the object
print(ContractNegotiation.to_json())

# convert the object into a dict
contract_negotiation_dict = contract_negotiation_instance.to_dict()
# create an instance of ContractNegotiation from a dict
contract_negotiation_from_dict = ContractNegotiation.from_dict(contract_negotiation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


