# ViewSet

## The Problem
If you review the [Generics](/DRF/generics.md) file, it has ended with two view classes:

```python
class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = "pk", this is the default
    lookup_url_kwarg = "pk"
```

We want to combine these classes, but, the limitation comes from the `urls.py` file.

```python
urlpatterns = [
    ...
    path("book/", BookListAPIView.as_view()),
    path("book/<int:pk>/", BookDetailAPIView.as_view()),
]
```

## The Solution
To solve the above problem, DRF suggests the `ViewSet` concept.

If we implement the view class as below, what is the problem?

```python
class BookAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
```

The `PROBLEM` is related to the `Method Resolution Order (MRO)`. Both `ListCreateAPIView` and `RetrieveUpdateDestroyAPIView` contain a `get` method. According to the order of father classes definition, always the `get` method of `ListCreateAPIView` will be executed, even for retrieving an item.

To solve the recent problem, the `ViewSetMixin` needs a parameter titled `actions`. This parameter shall be passed through the `.as_view` method in the `urls.py` file.

Actually, we shall define the mapping between the HTTP methods and our view methods.

```python
actions = { '<http_method_name>' : '<view_class_method_name>' }
```


## APIView vs ViewSet
`APIView` only understands the view class methods which their name are equal to the HTTP methods name. E.g. `get`, `post`, `put`, `patch`, and `delete`.

`ViewSet` is a bit more intelligent than APIView. It does not care about the name of methods defined in the view class. A python dictionary object titled `actions` shall be passed through the `as_view` method in the router (`urls.py` file).

Suppose you defined `get_all_books`, `create_a_book`, `retrieve`, `update`, `partial_update`, and `destroy` methods in the view class. Now, the `urls.py` file shall look like this:

```python
urlpatterns = [
    ...
    path("book/", BookListAPIView.as_view({
        'get':'get_all_books', 
        'post':'create_a_book',
    })),
    path("book/<int:pk>/", BookDetailAPIView.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy',
    })),
]
```


## ViewSet
This class inherits from `ViewSetMixin` and `APIView`.

Using ViewSet is a good habit. But why?


## GenericViewSet
This class inherits from `ViewSetMixin` and `GenericAPIView`.


## ViewSetMixin
See the `ViewSetMixin` codes at:
```python
from rest_framework.viewsets import ViewSetMixin
```

See lines number from 114 to 118.
```python
# Bind methods to actions
# This is the bit that's different to a standard view
for method, action in actions.items():
    handler = getattr(self, action)
    setattr(self, method, handler)
```
The mixin defines attributes with HTTP methods name and set their value with view class methods name.


## ReadOnlyModelViewSet
A viewset that provides default `list()` and `retrieve()` actions.


## ModelViewSet
A viewset that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions.

### Examples
```python
class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'kambiz'
```

```python
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
```


## Non-Model ViewSet

### Examples
```python
from datetime import datetime

from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet


class HelloViewSet(ViewSet):
    @action(detail=False)
    def greeting(self, request):
        return Response('Hello World')

    @action(detail=False)
    def time(self, request):
        return Response(datetime.now())
```

Then register the `HelloViewSet` in the urls.py file - see [Routers](/DRF/routers.md).