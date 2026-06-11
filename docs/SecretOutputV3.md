# SecretOutputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.secret_output_v3 import SecretOutputV3

# TODO update the JSON string below
json = "{}"
# create an instance of SecretOutputV3 from a JSON string
secret_output_v3_instance = SecretOutputV3.from_json(json)
# print the JSON string representation of the object
print(SecretOutputV3.to_json())

# convert the object into a dict
secret_output_v3_dict = secret_output_v3_instance.to_dict()
# create an instance of SecretOutputV3 from a dict
secret_output_v3_from_dict = SecretOutputV3.from_dict(secret_output_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


