# ParticipantContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**identity** | **str** |  | 
**properties** | **object** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from edc_client.models.participant_context import ParticipantContext

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantContext from a JSON string
participant_context_instance = ParticipantContext.from_json(json)
# print the JSON string representation of the object
print(ParticipantContext.to_json())

# convert the object into a dict
participant_context_dict = participant_context_instance.to_dict()
# create an instance of ParticipantContext from a dict
participant_context_from_dict = ParticipantContext.from_dict(participant_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


