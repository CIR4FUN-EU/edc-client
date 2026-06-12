# AssetProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conforms_to** | **str** |  | [optional] 

## Example

```python
from edc_client.models.asset_properties import AssetProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AssetProperties from a JSON string
asset_properties_instance = AssetProperties.from_json(json)
# print the JSON string representation of the object
print(AssetProperties.to_json())

# convert the object into a dict
asset_properties_dict = asset_properties_instance.to_dict()
# create an instance of AssetProperties from a dict
asset_properties_from_dict = AssetProperties.from_dict(asset_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


