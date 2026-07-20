# Serializer
resource: https://www.django-rest-framework.org/api-guide/serializers/

model --->SERIALIZER---> pure python type (usually dictionary) --->SOME MODULE methods (e.g. json.dump)---> json

The above overall process is not the serializer's responsibility.

Serializer will only convert a model instance to a pure python type (dict, list, etc.). The reason lies on:
1. Single Responsibility Principle (SRP)
2. Defining different parser than renderer. Maybe we want to convert to a different type than we received. It is not common, but in this way, we can receive XML and respond in json.

## Saving Instances
The `create` or `update` methods shall be defined in the serializer class to save an instance.

resource: https://www.django-rest-framework.org/api-guide/serializers/#saving-instances

## Passing Additional attributes to .save()
These additional attributes are available in the `validated_data` in the `create` or `update` methods.

resource: https://www.django-rest-framework.org/api-guide/serializers/#passing-additional-attributes-to-save


# ModelSerializer
`IMPORTANT` If the serializer field name is equal to the model name, the connection will be established automatically. Otherwise, pass an argument titled `source` following with the model field name.



### Examples
```python
# models.py

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=10)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```
#### Type 1
```python
# serializers.py

from rest_framework import serializers

from test_app.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
```
#### Output
![Model serializer type1](/DRF/serializers/model-serializer-type1-1.png)

`NOTE` The `full_name` property will not appear on GET results and the form to POST the data. Alternatively names in the fields options can map to properties or methods which take no arguments that exist on the model class.

resource: https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include


#### Type 2
To customize the fields to be shown or filled by user:
```python
# serializers.py

from rest_framework import serializers

from test_app.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # to include the properties, the fields shall be specified manually
        fields = ["id", "full_name", "first_name", "last_name", "slug"]
        # the order of fields in the above line,
        # defines the order of fields in the browseable api view
        extra_kwargs = {
            "full_name": {"read_only": True},
            "first_name": {"write_only": True},
            "last_name": {"write_only": True},
        }

# or


from rest_framework import serializers

from test_app.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, write_only=True)
    last_name = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = Author
        fields = ["id", "full_name", "slug", "first_name", "last_name"]
```
`OUTPUT`
![Model serializer type2](/DRF/serializers/model-serializer-type2-1.png)


## PrimaryKeyRelatedField
```python
class BookSerializer(serializers.ModelSerializer):
    # changing the type of a field
    # write the exact field name and override its model field
    # for example a field can be turned off
    # author = None  # to turn off a field 
    # the above line did not work, how can we turn it off with None?
    
    # all related fields type is PrimaryKeyRelatedField by default
    # the queryset is an essential parameter for RelatedField class
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    # a filter can be set on the queryset argument, 
    # queryset=Author.objects.filter(first_name__istartswith='j')
    # note that this queryset will be used by the serializer validator
    # when a new book is created by POST, if the author first_name
    # does not start with 'j', the validator raises an error that this
    # author is not in my database


    class Meta:
        model = Book
        fields = '__all__'
```

## StringRelatedField
```python
class BookSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # this field is read_only by default
    # the queryset is not required for read_only fields like StringRelatedField
    # it is not possible to add an Book using a string (not logical)
    # now the author field of the model has been overridden
    # if you want to add another book (POST), 
    # the author field can not receive data due to StringRelatedField type
    # to solve this, add another field like below:
    # author_pk = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)

    # below changes will make things prettier
    author_name = serializers.StringRelatedField(source='author')
    # author_name represents the author name
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)
    # now author can receive data


    class Meta:
        model = Book
        fields = '__all__'
```

## SlugRelatedField
```python
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=10, unique=True)
```
```python
class AuthorCreateWithFullnameSerializer(serializers.Serializer):
    # the below order defines the order of presentation in the browseable api view
    id = serializers.BigIntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    fullname = serializers.CharField(min_length=10, max_length=250, required=True)
    slug = serializers.CharField(max_length=10)
```
```python
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='slug',
    )
    # queryset and slug_field are needed
    # the slug_field is needed to compare the input data with the corresponding
    # field, not the id
    # like id, it can be stored with a keyword, a slug field shall be
    # added to the model which must be unique and not bland
    # id is an integer, but slug is a meaningful string


    class Meta:
        model = Book
        fields = '__all__'
```

## HyperlinkedRelatedField
```python
class BookSerializer(serializers.ModelSerializer):
    # author_name = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail',
    # )
    # the view_name is required as a string to create the link

    # or
    author_link = serializers.HyperlinkedRelatedField(
        view_name='author-detail',
        # if the view receives a lookup_url_kwarg other than default (pk),
        # pass the relevant parameter
        # lookup_url_kwarg='kambiz',
        source='author',
        read_only=True,  # it is hard to create with hyperlink
    )
    author = serializers.StringRelatedField()
    author_pk = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True,
    )


    class Meta:
        model = Book
        fields = '__all__'
```

## HyperlinkedModelSerializer



## Meta

### model

### fields

### exclude

### extra_kwargs
resource: https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

### read_only_fields
resource: https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields

### depth
It is used to represent the instance instead of pk, string, slug, or hyperlink.

```python
# type 1

class BookSerializer(serializers.ModelSerializer):
    author = AuthorCreateWithFullnameSerializer()
    # can we load it lazy?


    class Meta:
        model = Book
        fields = '__all__'
```

```python
# type 2

class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
        # defines the level of related fields
        # with read_only = True
        # default is depth = 0
```

### `SOFTWARE ENGINEERING, API DESIGN` 
APIs with deep layers of instances is not reasonable!
- Depth is infinite, there is no end for it.
- Data volume increases, causes the data transferring slow.

`SOLUTION` Use id instead of depth alongside with a list of ids. Provide an API for a list of ids to be used by a frontend developer.


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
        # the above return will produce a different 
        # output in the browseable api view
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
|source|str|the model field name|
|view_name|str|to create the hyperlink|

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

## SerializerMethodField
resource: https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield


# Nested Serializer
The related field shall receive an instance of serializer class.
```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'slug']


class BookSerializer(serializer.ModelSerializer):
    # suppose that `a` is a related field
    author = AuthorSerializer()
    # now, a nested serializer is defined
    

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

## Nested ReadOnly
```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'slug']


class BookSerializer(serializer.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

The `author` is a read only field. To create a book, an author shall be defined. However, it is not possible with the above version. A new write only field shall be defined.

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'slug']


class BookSerializer(serializer.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_slug = serializers.SlugRelatedField(
        slug_field='slug',
        source='author',
        queryset=Author.objects.all(),
        write_only=True,
    )
    

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_slug']
```

## Nested Writable
```python
# serializers.py

class AuthorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'slug', 'fullname']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorMiniSerializer()

    class Meta:
        model = Book
        fields = '__all__'
```

Now, to create a new book, the browseable api view receives the author as below:
```
{
    'author': {
        'slug': ''
    },
    'title': '',
    'categories': []
}
```

An error will be raised that `create` and `update` methods shall be implemented. What I understand is that, the BookSerializer is only able to create Book instances, not the Author ones. To enable this feature, the `create` and `update` methods shall be overridden.

```python
# serializers.py

class AuthorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'slug', 'fullname']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorMiniSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')  # is a dictionary
        # the author, which is the nested field shall be popped
        # to prevent the construction of this field in the super().create()
        # and to prevent raising the exception

        # two options may happen, the user may send
        # a name of a new author
        # or
        # a name of a existed author
        author, _ = Author.objects.get_or_create(
            slug=author_data['slug'], 
            defaults=author_data
        )
        
        # the super().create() is needed for constructing other fields
        validated_data['author'] = author
        return super().create(validated_data)
        # or
        # implement the create yourself

    # a same scenario shall be performed for update method
    def update(self, instance, validated_data):
        if 'author' in validated_data:
            author_data = validated_data.pop('author')
            Author.objects.update_or_create(
                slug=author_data['slug'],
                defaults=author_data,
            )
            instance.author = Author.objects.get(slug=author_data['slug'])
        return super().update(instance, validated_data)
        # may raise uniqueness error, override the slug field in the serializer
```


# Serializer Validation
It is possible to pass built-in or customized validators to the serializer class. See the docs.

resource: https://www.django-rest-framework.org/api-guide/serializers/#validators

To implement a validator, it shall inherits from `BaseValidator`. See the doc.

`NOTE` If there are numerous serializer and validators, it is recommended to define a class for your own validators.

## Field-Level Validation
resource: https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation

`NOTE` Field validators will be run prior to Object validators.

## Object-Level Validation
resource: https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation

`NOTE` The request may come from the create or update methods. The DRF distinguish this by the presence of `instance` attribute.


# Extra Context
resource: https://www.django-rest-framework.org/api-guide/serializers/#including-extra-context
