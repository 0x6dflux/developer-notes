model --->SERIALIZER---> pure python type (usually dictionary) --->SOME MODULE methods (e.g. json.dump)---> json

The above overall process is not the serializer's responsibility.

Serializer will only convert a model instance to a pure python type (dict, list, etc.). The reason lies on:
1. Single Responsibility Principle (SRP)
2. Defining different parser than renderer. Maybe we want to convert to a different type than we received. It is not common, but in this way, we can receive XML and respond in json.

## Parameters
In view, when we are instantiating a serializer, bare in mind:
- `instance` parameter is used for receiving a model object (usually in GET).
- `data` parameter is used for passing a request data (usually in POST).
    - Do not forget that in `PUT` and `PATCH` methods, the above parameters shall be given. In this way, the ModelSerializer is able to compare these values (by serializer validator, is_valid()). For `PUT` method, all fields shall be passed - look at the description provided in `partial:bool`.
- `many:bool` parameter is used to indicate that the inputted instance is a collection of objects. So, DRF will use a ListSerializer.
- `partial:bool` will inform the serializer validator (is_valid()) that sending all fields by user is necessary or not. For `PUT` method, this parameter is `False` (which the default value); for `PATCH` method, this parameter shall be set to `True`.


it is possible to pass a context to a serializer
as well as paginating!!