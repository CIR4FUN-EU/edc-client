# DiscoveryResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**profile** | **str** | The local dataspace profile id that matches a protocol version advertised by the counter party. | 
**version** | **str** | The DSP protocol version shared by the local profile and the counter party entry. | 
**counter_party** | [**CounterParty**](CounterParty.md) |  | 
**binding** | **str** | The protocol binding for this match (copied from the counter party version entry). | 

## Example

```python
from openapi_client.models.discovery_response_schema import DiscoveryResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryResponseSchema from a JSON string
discovery_response_schema_instance = DiscoveryResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DiscoveryResponseSchema.to_json())

# convert the object into a dict
discovery_response_schema_dict = discovery_response_schema_instance.to_dict()
# create an instance of DiscoveryResponseSchema from a dict
discovery_response_schema_from_dict = DiscoveryResponseSchema.from_dict(discovery_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


