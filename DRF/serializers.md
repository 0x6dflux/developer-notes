# Serializer
model --->SERIALIZER---> pure python type (usually dictionary) --->SOME MODULE methods (e.g. json.dump)---> json

The above overall process is not the serializer's responsibility.

Serializer will only convert a model instance to a pure python type (dict, list, etc.). The reason lies on:
1. Single Responsibility Principle (SRP)
2. Defining different parser than renderer. Maybe we want to convert to a different type than we received. It is not common, but in this way, we can receive XML and respond in json.


# ModelSerializer
```python

```

## Parameters
In view, when we are instantiating a serializer, bare in mind:
- `instance` parameter is used for receiving a model object (usually in GET).
- `data` parameter is used for passing a request data (usually in POST).
    - Do not forget that in `PUT` and `PATCH` methods, the above parameters shall be given. In this way, the ModelSerializer is able to compare these values (by serializer validator, is_valid()). For `PUT` method, all fields shall be passed - look at the description provided in `partial:bool`.
- `many:bool` parameter is used to indicate that the inputted instance is a collection of objects. So, DRF will use a ListSerializer.
- `partial:bool` will inform the serializer validator (is_valid()) that sending all fields by user is necessary or not. For `PUT` method, this parameter is `False` (which the default value); for `PATCH` method, this parameter shall be set to `True`.


it is possible to pass a context to a serializer
as well as paginating!!



# Serializer
`QUESTION` What if the model does not have a field, e.g. full_name? Or a field is defined as a property (getter) and does not support the setter!? How about setting a value to this property by user?

`QUESTION` What if we do not have a model?

`QUESTION` Maybe we do not want to use the ModelSerializer and want to create our own Serializer!

```python
# example

from rest_framework import serializers


class AuthorCreateWithFullnameSerializer(serializers.Serializer):
    fullname = serializers.CharField(min_length=10, max_length=250)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=10, max_length=250, required=True)
    password = serializers.CharField(min_length=10, max_length=250, required=True, write_only=True)
```

`VERY IMPORTANT` Do not forget to implement the `create` and `update` methods.

`IMPORTANT` Serializer is a two-way class: (JSON, XML, etc.) `Defined Type ⇋ Pure Python Type` (dict, list, etc.)

`FileField` To send or show a file (two-way)

`FilePathField`

`EmailField` Same as `CharField`, but, with an `EmailValidator` (like forms)

`ReadOnlyField` Just to show to user in response, e.g. id. `id` is a read_only field by default; if you send a value for it in a request, the serializer will skip it.

### create and update
`HINT` Have a look at `ModelSerializer`.

```python
class AuthorCreateWithFullnameSerializer(serializers.Serializer):
    # the below order defines the order of presentation in the browseable api view
    id = serializers.BigIntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    fullname = serializers.CharField(min_length=10, max_length=250, required=True)

    # validated_data: dict
    def create(self, validated_data):
        name_parts = validated_data['fullname'].split(' ')
        # insert query on database shall be implemented
        return Author.objects.create(
            first_name=name_parts[0],
            last_name=name_parts[1],
        )

    def update(self, instance, validate_data):
        name_parts = validated_data['fullname'].split(' ')
        # in this case, instance: Author
        instance.first_name = name_parts[0]
        instance.last_name = name_parts[1]
        # update query on database shall be implemented
        instance.save()
        # instance shall be returned
        return instance
```
----
### `DESIGN TIP`
The above solution, is what DRF provided due to simplicity, not the best design.

Instead, every steps defined above, shall be implemented in view (maybe without using ViewSet, which requires writing more codes). 

```python
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateWithFullnameSerializer

    # this below method shall be overridden 
    # to define what our business logic wants 
    def perform_create(self, serializer):
        # what we have written in the serializer create method
        name_parts = serializer.validated_data['fullname'].split(' ')
        # to have the same output like ModelSerializer after 
        # hitting the POST button, we shall update the serializer instance
        serializer.instance = Author.objects.create(
            first_name=name_parts[0],
            last_name=name_parts[1],
        )
        # return Author.objects.create(
        #     first_name=name_parts[0],
        #     last_name=name_parts[1],
        # )
```

As per modern design principles (separation of concerns), saving on database in a UI layer is not a good practice. 

Since the `serializer is a UI layer`, saving on database shall not be implemented in the serializer class. Another layer shall take care of this responsibility in the multi-layer architecture.

Serializer is responsible for getting the inputs, performing some simple and basic validations (e.g. does the email contain @ sign, is the domain included in the email), etc. In the above case, a validation shall be defined in the serializer to check that whether the fullname field contains only one space or not. This validation belongs to the serializer.

But, serializers shall not contain all validations. Complex validations which requires reading data (e.g. if a product is available in the inventory, extend this example for websites like Amazon or Digikala), shall not be checked in the serializer. In general, any kind of business logic shall not be written in the serializer; perhaps, to be implemented in a view - which still is not the bast place, but better than serializer.

This tip is also valid for the update method!

----


## Field
The parent class of other serializer fields. Its parameters shall be pass only with kwargs.

|Parameters|Type|Description|
|--:|:--|:--|
|read_only|bool||
|write_only|bool||
|required|bool||
|default||shall be set if the field is required|
|validators|||

`IMPORTANT` Read and understand the codes provided for `Field`. For example, read_only and write_only can be True simultaneously, there is an assert expression for it. Another example is required and default.

`write_only` Do not show it in response. But, in a request, the user can set its value, and will be analyze by serializer, and so on.

## CharField
|Parameters|Type|Description|
|--:|:--|:--|
|allow_blank|bool||
|trim_whitespace|bool|to trim start and end|
|max_length|int||
|min_length|int||
||||