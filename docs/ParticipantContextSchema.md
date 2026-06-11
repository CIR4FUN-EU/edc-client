# ParticipantContextSchema


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
from openapi_client.models.participant_context_schema import ParticipantContextSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantContextSchema from a JSON string
participant_context_schema_instance = ParticipantContextSchema.from_json(json)
# print the JSON string representation of the object
print(ParticipantContextSchema.to_json())

# convert the object into a dict
participant_context_schema_dict = participant_context_schema_instance.to_dict()
# create an instance of ParticipantContextSchema from a dict
participant_context_schema_from_dict = ParticipantContextSchema.from_dict(participant_context_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


