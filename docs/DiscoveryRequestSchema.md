# DiscoveryRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**counter_party_id** | **str** | The counter party&#39;s DID. The DID is resolved and the &#39;DataService&#39; entry of the DID document provides the base URL of the well-known endpoint. | [optional] 
**counter_party_address** | **str** | The counter party&#39;s discovery URL pointing directly at the &#39;/.well-known/dspace-version&#39; endpoint, or the host that serves it. Takes precedence over counterPartyId. | [optional] 

## Example

```python
from edc_client.models.discovery_request_schema import DiscoveryRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryRequestSchema from a JSON string
discovery_request_schema_instance = DiscoveryRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DiscoveryRequestSchema.to_json())

# convert the object into a dict
discovery_request_schema_dict = discovery_request_schema_instance.to_dict()
# create an instance of DiscoveryRequestSchema from a dict
discovery_request_schema_from_dict = DiscoveryRequestSchema.from_dict(discovery_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


