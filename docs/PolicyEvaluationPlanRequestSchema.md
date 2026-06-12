# PolicyEvaluationPlanRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**policy_scope** | **str** |  | 

## Example

```python
from edc_client.models.policy_evaluation_plan_request_schema import PolicyEvaluationPlanRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyEvaluationPlanRequestSchema from a JSON string
policy_evaluation_plan_request_schema_instance = PolicyEvaluationPlanRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyEvaluationPlanRequestSchema.to_json())

# convert the object into a dict
policy_evaluation_plan_request_schema_dict = policy_evaluation_plan_request_schema_instance.to_dict()
# create an instance of PolicyEvaluationPlanRequestSchema from a dict
policy_evaluation_plan_request_schema_from_dict = PolicyEvaluationPlanRequestSchema.from_dict(policy_evaluation_plan_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


