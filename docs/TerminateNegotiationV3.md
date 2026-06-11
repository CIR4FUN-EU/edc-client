# TerminateNegotiationV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.terminate_negotiation_v3 import TerminateNegotiationV3

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateNegotiationV3 from a JSON string
terminate_negotiation_v3_instance = TerminateNegotiationV3.from_json(json)
# print the JSON string representation of the object
print(TerminateNegotiationV3.to_json())

# convert the object into a dict
terminate_negotiation_v3_dict = terminate_negotiation_v3_instance.to_dict()
# create an instance of TerminateNegotiationV3 from a dict
terminate_negotiation_v3_from_dict = TerminateNegotiationV3.from_dict(terminate_negotiation_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


