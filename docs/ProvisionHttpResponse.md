# ProvisionHttpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_address** | [**DataAddress1**](DataAddress1.md) |  | [optional] 

## Example

```python
from openapi_client.models.provision_http_response import ProvisionHttpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionHttpResponse from a JSON string
provision_http_response_instance = ProvisionHttpResponse.from_json(json)
# print the JSON string representation of the object
print(ProvisionHttpResponse.to_json())

# convert the object into a dict
provision_http_response_dict = provision_http_response_instance.to_dict()
# create an instance of ProvisionHttpResponse from a dict
provision_http_response_from_dict = ProvisionHttpResponse.from_dict(provision_http_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


