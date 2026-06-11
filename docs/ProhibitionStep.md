# ProhibitionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | [optional] 
**rule_functions** | **List[str]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.prohibition_step import ProhibitionStep

# TODO update the JSON string below
json = "{}"
# create an instance of ProhibitionStep from a JSON string
prohibition_step_instance = ProhibitionStep.from_json(json)
# print the JSON string representation of the object
print(ProhibitionStep.to_json())

# convert the object into a dict
prohibition_step_dict = prohibition_step_instance.to_dict()
# create an instance of ProhibitionStep from a dict
prohibition_step_from_dict = ProhibitionStep.from_dict(prohibition_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


