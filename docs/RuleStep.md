# RuleStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_filtered** | **bool** |  | [optional] 
**filtering_reasons** | **List[str]** |  | [optional] 
**constraint_steps** | [**List[ConstraintStep]**](ConstraintStep.md) |  | [optional] 
**rule_functions** | **List[str]** |  | [optional] 

## Example

```python
from edc_client.models.rule_step import RuleStep

# TODO update the JSON string below
json = "{}"
# create an instance of RuleStep from a JSON string
rule_step_instance = RuleStep.from_json(json)
# print the JSON string representation of the object
print(RuleStep.to_json())

# convert the object into a dict
rule_step_dict = rule_step_instance.to_dict()
# create an instance of RuleStep from a dict
rule_step_from_dict = RuleStep.from_dict(rule_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


