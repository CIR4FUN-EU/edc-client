# RootDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**distribution** | [**List[Distribution]**](Distribution.md) |  | [optional] 
**has_policy** | [**List[Offer]**](Offer.md) |  | 
**context** | **List[str]** |  | 

## Example

```python
from openapi_client.models.root_dataset import RootDataset

# TODO update the JSON string below
json = "{}"
# create an instance of RootDataset from a JSON string
root_dataset_instance = RootDataset.from_json(json)
# print the JSON string representation of the object
print(RootDataset.to_json())

# convert the object into a dict
root_dataset_dict = root_dataset_instance.to_dict()
# create an instance of RootDataset from a dict
root_dataset_from_dict = RootDataset.from_dict(root_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


