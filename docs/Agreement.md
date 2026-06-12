# Agreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**profile** | [**PolicyClassProfile**](PolicyClassProfile.md) |  | [optional] 
**permission** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibition** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**obligation** | [**List[Duty]**](Duty.md) |  | [optional] 
**type** | **str** |  | 
**target** | **str** |  | 
**assigner** | **str** |  | 
**assignee** | **str** |  | 
**timestamp** | **str** |  | [optional] 

## Example

```python
from edc_client.models.agreement import Agreement

# TODO update the JSON string below
json = "{}"
# create an instance of Agreement from a JSON string
agreement_instance = Agreement.from_json(json)
# print the JSON string representation of the object
print(Agreement.to_json())

# convert the object into a dict
agreement_dict = agreement_instance.to_dict()
# create an instance of Agreement from a dict
agreement_from_dict = Agreement.from_dict(agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


