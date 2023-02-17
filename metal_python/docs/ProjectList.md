# ProjectList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**projects** | [**List[Project]**](Project.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from metal_python.models.project_list import ProjectList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectList from a JSON string
project_list_instance = ProjectList.from_json(json)
# print the JSON string representation of the object
print ProjectList.to_json()

# convert the object into a dict
project_list_dict = project_list_instance.to_dict()
# create an instance of ProjectList from a dict
project_list_form_dict = project_list.from_dict(project_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

