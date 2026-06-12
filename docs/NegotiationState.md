# NegotiationState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**state** | **str** |  | 

## Example

```python
from edc_client.models.negotiation_state import NegotiationState

# TODO update the JSON string below
json = "{}"
# create an instance of NegotiationState from a JSON string
negotiation_state_instance = NegotiationState.from_json(json)
# print the JSON string representation of the object
print(NegotiationState.to_json())

# convert the object into a dict
negotiation_state_dict = negotiation_state_instance.to_dict()
# create an instance of NegotiationState from a dict
negotiation_state_from_dict = NegotiationState.from_dict(negotiation_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


