# DistributionAccessService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**endpoint_url** | **str** |  | 
**serves_dataset** | [**List[Dataset]**](Dataset.md) |  | [optional] 

## Example

```python
from openapi_client.models.distribution_access_service import DistributionAccessService

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionAccessService from a JSON string
distribution_access_service_instance = DistributionAccessService.from_json(json)
# print the JSON string representation of the object
print(DistributionAccessService.to_json())

# convert the object into a dict
distribution_access_service_dict = distribution_access_service_instance.to_dict()
# create an instance of DistributionAccessService from a dict
distribution_access_service_from_dict = DistributionAccessService.from_dict(distribution_access_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


