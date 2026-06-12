# CounterParty

Counter party coordinates for a matched protocol version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path under the counter party&#39;s base URL where the matching DSP version is exposed, as returned in the well-known versions document. | 
**data_service_endpoint** | **str** | The counter party&#39;s data service endpoint URL. | [optional] 

## Example

```python
from edc_client.models.counter_party import CounterParty

# TODO update the JSON string below
json = "{}"
# create an instance of CounterParty from a JSON string
counter_party_instance = CounterParty.from_json(json)
# print the JSON string representation of the object
print(CounterParty.to_json())

# convert the object into a dict
counter_party_dict = counter_party_instance.to_dict()
# create an instance of CounterParty from a dict
counter_party_from_dict = CounterParty.from_dict(counter_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


