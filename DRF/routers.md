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