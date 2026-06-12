# SecretInputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from edc_client.models.secret_input_v3 import SecretInputV3

# TODO update the JSON string below
json = "{}"
# create an instance of SecretInputV3 from a JSON string
secret_input_v3_instance = SecretInputV3.from_json(json)
# print the JSON string representation of the object
print(SecretInputV3.to_json())

# convert the object into a dict
secret_input_v3_dict = secret_input_v3_instance.to_dict()
# create an instance of SecretInputV3 from a dict
secret_input_v3_from_dict = SecretInputV3.from_dict(secret_input_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


