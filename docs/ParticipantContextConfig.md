# ParticipantContextConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**entries** | **object** |  | 
**private_entries** | **object** |  | [optional] 

## Example

```python
from edc_client.models.participant_context_config import ParticipantContextConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantContextConfig from a JSON string
participant_context_config_instance = ParticipantContextConfig.from_json(json)
# print the JSON string representation of the object
print(ParticipantContextConfig.to_json())

# convert the object into a dict
participant_context_config_dict = participant_context_config_instance.to_dict()
# create an instance of ParticipantContextConfig from a dict
participant_context_config_from_dict = ParticipantContextConfig.from_dict(participant_context_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


