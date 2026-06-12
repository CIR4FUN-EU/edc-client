# AssetOutputV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**data_address** | [**DataAddress**](DataAddress.md) |  | [optional] 
**private_properties** | **Dict[str, object]** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 

## Example

```python
from edc_client.models.asset_output_v3 import AssetOutputV3

# TODO update the JSON string below
json = "{}"
# create an instance of AssetOutputV3 from a JSON string
asset_output_v3_instance = AssetOutputV3.from_json(json)
# print the JSON string representation of the object
print(AssetOutputV3.to_json())

# convert the object into a dict
asset_output_v3_dict = asset_output_v3_instance.to_dict()
# create an instance of AssetOutputV3 from a dict
asset_output_v3_from_dict = AssetOutputV3.from_dict(asset_output_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


