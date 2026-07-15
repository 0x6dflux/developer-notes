# DRF Exceptions

link to [Django Exceptions](../Django/exceptions.md)

an standard for errors shall be stablish.
learn how to customize an exception_handler to raise a 404 error instead of 500!!

in APIView, there is a method to get an exception_handler!!!

# List of Exceptions

## ViewSet Exceptions
###### #1
Suppose you have added a method name, e.g. 'asghar', in the `actions` argument, but this method is not defined in the view class. So, ViewSet will raise the following exception:

![Method Not Found](/DRF/exceptions/viewset_exceptions/method-not-found-1.png)
![Method Not Found](/DRF/exceptions/viewset_exceptions/method-not-found-2.png)

ViewSet will verify methods name in advance, please see the code.

###### #2
Suppose you have defined an unknown HTTP method in the `actions` argument, e.g. `{..., 'asghar': 'perform_update'}`. ViewSet will ignore this method.

`CONCLUSION` DRF ViewSet checks the view class methods name, but does not care about undefined HTTP methods.

###### #3
Suppose you mis-mapped a method to a wrong HTTP method, E.g. `'get': 'perform_update`.

![Mis-Mapped Method](/DRF/exceptions/viewset_exceptions/mis-mapped-method-1.png)

This exception is true, since, to retrieve an item, an identifier is needed. But, perform_update is not related to this HTTP method.

###### #4
This exception is originated from the lines where a method is defined in a ViewSet class, and the `return` clause has been missed.

![Expected a response](/DRF/exceptions/viewset_exceptions/expected-a-response-1.png)


## Serializer Exceptions
###### #1
All serializers shall define the create method, otherwise the `BaseSerializer` class will raise the following error. Even, the `ModelSerializer` and `ListSerializer` have defined this method.

![Create() must be implemented ](/DRF/exceptions/serializers_exceptions/create-not-implemented-1.png)
![Create() must be implemented ](/DRF/exceptions/serializers_exceptions/create-not-implemented-2.png)


###### #2
The `queryset` parameter is not required for `read_only` fields, e.g. `StringRelatedField`.

![No queryset is needed for read_only fields](/DRF/exceptions/serializers_exceptions/read-only-fields-do-not-require-queryset-1.png)


###### #2
The HyperlinkedRelatedField requires `view_name` parameter.

![View name is required](/DRF/exceptions/serializers_exceptions/view-name-is-required-1.png)


## Routers Exceptions
###### #1
When defining a non-model viewset, the router is not able to get the model name to set the basename parameter in generating the urls.

![Basename not specified](/DRF/exceptions/routers_exceptions/basename-not-specified-1.png)


## Exception Handling