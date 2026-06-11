# ContractRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddress1]**](CallbackAddress1.md) |  | [optional] 
**counter_party_address** | **str** |  | 
**policy** | [**OfferV3**](OfferV3.md) |  | 
**protocol** | **str** |  | 

## Example

```python
from openapi_client.models.contract_request_v3 import ContractRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of ContractRequestV3 from a JSON string
contract_request_v3_instance = ContractRequestV3.from_json(json)
# print the JSON string representation of the object
print(ContractRequestV3.to_json())

# convert the object into a dict
contract_request_v3_dict = contract_request_v3_instance.to_dict()
# create an instance of ContractRequestV3 from a dict
contract_request_v3_from_dict = ContractRequestV3.from_dict(contract_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


