# Routers

## SimpleRouter
Add below lines to the `urls.py` file.

```python
from rest_framework.routers import SimpleRouter

from tutorial.views import AuthorAPIView, BookAPIView


router = SimpleRouter(use_regex_path=False)
router.register(prefix='book', viewset=BookAPIView)
router.register(prefix='author', viewset=AuthorAPIView)

urlpatterns = [
    ...
]

urlpatterns += router.urls
```

`IMPORTANT` The router will set a default `lookup_url_kwarg`, unless you define it in your viewset class.

`Note` A breadcrumb has been created at top.

## DefaultRouter
Same as SimpleRouter, but, adds a root url to show a list of urls in the browseable api view (useful for documenting and giving help on the provided API).

### Example
```python
from rest_framework.routers import DefaultRouter


router = DefaultRouter(user_regex_path=False)
router.register('book', BookAPIView, basename='book')
router.register(prefix='author', viewset=AuthorViewSet)
# passing basename argument is essential for the below line,
# since the viewset is not a ModelViewSet
router.register(prefix='system', viewset=HelloViewSet, basename='system')


urlpatterns = [
    ...
]

urlpatterns += router.urls
```

`NOTE` The system url has not been added to the root url - perhaps, due to the fact, that this is not related to any model.

## BaseRouter
### basename Parameter
It is similar to namespace and creates `name` argument for path. As default, the `BaseRouter` sets the model name as the basename, unless you specify it.

To set the model name as the basename, the BaseRouter needs the queryset attribute which is defined by `GenericAPIView`. If your view class does not inherit from the GenericAPIView class, the BaseRouter will raise an error.

`IMPORTANT` The BaseRouter will check the uniqueness of the basename in the current router object. If there is another router instance, the BaseRouter can not cross check the basename.

`IMPORTANT` The BaseRouter sets a `urls` attribute to cache the urls. This prevents the heavy computation of generating the urls. On the other hand, to register the urls (generating urls), the `register` method of the BaseRouter will delete the cached urls. This assures that previous urls to be checked against new urls.


## DynamicRoute
`CHALLENGE` Suppose you want to add other actions, other than CRUD actions, to your API, e.g. getting the recent 3 books. Or, you want to name your CRUD actions sth else, e.g. get_book (instead of list) and create_a_book (instead of create).

In the above cases, the `SimpleRouter` and `DefaultRouter` does not work.

The `SOLUTION` is the `DynamicRoute`. A dynamic route can be defined using a decorator called `@action`. This decorator receives parameters, like `methods`, `detail` which is required, `url_path`, and `url_name`. `url_path` and `url_name` will be set by method name by default, unless you specify them. Other viewset-level attributes (*_classes, e.g. renderer_classes) can be passed to the action decorator. Be careful, some classes shall be callable and not a string.

```python
from rest_framework.decorators import action

@action(methods=['get'], detail=False, url_path='recent', renderer_classes=[XMLRenderer])
def get_recent_books(self, request):
    q = self.get_queryset().order_by('-id')[:3]
    s = self.get_serializer(q, many=True)

    return Response(s.data)
```

`ADVICE` Review the lines of codes where DRF generates static and dynamic routes.


## QUESTION
How does DRF lazily import renderer_classes from the settings, but, the renderer_classes argument shall not be lazily passed when a method is decorated by `@action`?

`SOLUTION` The renderer_classes belongs to line 108 of `rest_framework.views` which loads its value from settings by default. In `APIView(View)` class definition, line 266, it tries to instantiate from the renderer_classes. If an string value to be given for this attribute,an exception an exception will be raised indicating that str is not callable. Note that, in settings, the default values for this attribute shall be set in string. What is the difference?

There is an extra process for getting default values from settings. This process is defined in the `rest_framework.settings` file where the APISettings class has been defined: 
- The `__getattr__` method has been overridden.
- Checks `if attr in self.import_strings` - line 229
- The list of `IMPORT_STRINGS` can be found in line 136
- Then it run `perform_import` method - line 163
- The class will be extracted by `import_from_string` method - line 177
- The `import_string` method will be run - line 19
- The import_string method will find the module and perform `cached_import` method (line 8)
- Finally, the `import_module` will be run from `importlib` - `from importlib import import_module`

`NOTE` All process will be occurred in line 108 of `rest_framework.views`.


## Extra Exercises
```python
from rest_framework.decorators import action


class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'kambiz'

    @action(methods=['get'], detail=False, url_path='recent', renderer_classes=[XMLRenderer])
    def ger_recent_book(self, request):
        q = self.get_queryset().order_by('-id')[:3]
        s = self.get_serializer(q, many=True)

        return Response(s.data)
```

```python
from rest_framework.decorators import action


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True)
    def books(self, request, pk):
        author = self.get_object()
        book_serializer = BookSerializer(author.book_set.all(), many=True)
        # self.get_serializer() is not true in this case,
        # since it will return the serializer related to Author

        return Response(book_serializer.data)
```
