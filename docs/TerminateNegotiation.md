# TerminateNegotiation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.terminate_negotiation import TerminateNegotiation

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateNegotiation from a JSON string
terminate_negotiation_instance = TerminateNegotiation.from_json(json)
# print the JSON string representation of the object
print(TerminateNegotiation.to_json())

# convert the object into a dict
terminate_negotiation_dict = terminate_negotiation_instance.to_dict()
# create an instance of TerminateNegotiation from a dict
terminate_negotiation_from_dict = TerminateNegotiation.from_dict(terminate_negotiation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


