# PolicyEvaluationPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**policy_scope** | **str** |  | 

## Example

```python
from edc_client.models.policy_evaluation_plan_request import PolicyEvaluationPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyEvaluationPlanRequest from a JSON string
policy_evaluation_plan_request_instance = PolicyEvaluationPlanRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyEvaluationPlanRequest.to_json())

# convert the object into a dict
policy_evaluation_plan_request_dict = policy_evaluation_plan_request_instance.to_dict()
# create an instance of PolicyEvaluationPlanRequest from a dict
policy_evaluation_plan_request_from_dict = PolicyEvaluationPlanRequest.from_dict(policy_evaluation_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


