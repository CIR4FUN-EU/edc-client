# AssetInputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**data_address** | [**DataAddress**](DataAddress.md) |  | 
**private_properties** | **Dict[str, object]** |  | [optional] 
**properties** | **Dict[str, object]** |  | 

## Example

```python
from edc_client.models.asset_input_v3 import AssetInputV3

# TODO update the JSON string below
json = "{}"
# create an instance of AssetInputV3 from a JSON string
asset_input_v3_instance = AssetInputV3.from_json(json)
# print the JSON string representation of the object
print(AssetInputV3.to_json())

# convert the object into a dict
asset_input_v3_dict = asset_input_v3_instance.to_dict()
# create an instance of AssetInputV3 from a dict
asset_input_v3_from_dict = AssetInputV3.from_dict(asset_input_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


