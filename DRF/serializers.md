model --->SERIALIZER---> pure python type (usually dictionary) --->SOME MODULE methods (e.g. json.dump)---> json

The above overall process is not the serializer's responsibility.

Serializer will only convert a model instance to a pure python type (dict, list, etc.). The reason lies on:
1. Single Responsibility Principle (SRP)
2. Defining different parser than renderer. Maybe we want to convert to a different type than we received. It is not common, but in this way, we can receive XML and respond in json.

## Parameters
In view, when we are instantiating a serializer, bare in mind:
- `instance` parameter is used for receiving a model object (usually in GET)
- `data` parameter is used for passing a request data (usually in POST)
- `many` parameter is used to indicate that the inputted instance is a collection of objects. So, DRF will use a ListSerializer.