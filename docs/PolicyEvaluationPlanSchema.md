# PolicyEvaluationPlanSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**pre_validators** | **List[str]** |  | [optional] 
**post_validators** | **List[str]** |  | [optional] 
**permission_steps** | [**List[PermissionStep]**](PermissionStep.md) |  | [optional] 
**prohibition_steps** | [**List[ProhibitionStep]**](ProhibitionStep.md) |  | [optional] 
**duty_steps** | [**List[DutyStep]**](DutyStep.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_evaluation_plan_schema import PolicyEvaluationPlanSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyEvaluationPlanSchema from a JSON string
policy_evaluation_plan_schema_instance = PolicyEvaluationPlanSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyEvaluationPlanSchema.to_json())

# convert the object into a dict
policy_evaluation_plan_schema_dict = policy_evaluation_plan_schema_instance.to_dict()
# create an instance of PolicyEvaluationPlanSchema from a dict
policy_evaluation_plan_schema_from_dict = PolicyEvaluationPlanSchema.from_dict(policy_evaluation_plan_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


