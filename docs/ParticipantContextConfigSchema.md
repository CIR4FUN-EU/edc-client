# ParticipantContextConfigSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**entries** | **object** |  | 
**private_entries** | **object** |  | [optional] 

## Example

```python
from edc_client.models.participant_context_config_schema import ParticipantContextConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantContextConfigSchema from a JSON string
participant_context_config_schema_instance = ParticipantContextConfigSchema.from_json(json)
# print the JSON string representation of the object
print(ParticipantContextConfigSchema.to_json())

# convert the object into a dict
participant_context_config_schema_dict = participant_context_config_schema_instance.to_dict()
# create an instance of ParticipantContextConfigSchema from a dict
participant_context_config_schema_from_dict = ParticipantContextConfigSchema.from_dict(participant_context_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


