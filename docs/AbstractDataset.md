# AbstractDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**distribution** | [**List[Distribution]**](Distribution.md) |  | [optional] 

## Example

```python
from openapi_client.models.abstract_dataset import AbstractDataset

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractDataset from a JSON string
abstract_dataset_instance = AbstractDataset.from_json(json)
# print the JSON string representation of the object
print(AbstractDataset.to_json())

# convert the object into a dict
abstract_dataset_dict = abstract_dataset_instance.to_dict()
# create an instance of AbstractDataset from a dict
abstract_dataset_from_dict = AbstractDataset.from_dict(abstract_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


