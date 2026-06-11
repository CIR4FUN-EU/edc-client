# SecretSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **List[str]** |  | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.secret_schema import SecretSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SecretSchema from a JSON string
secret_schema_instance = SecretSchema.from_json(json)
# print the JSON string representation of the object
print(SecretSchema.to_json())

# convert the object into a dict
secret_schema_dict = secret_schema_instance.to_dict()
# create an instance of SecretSchema from a dict
secret_schema_from_dict = SecretSchema.from_dict(secret_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


