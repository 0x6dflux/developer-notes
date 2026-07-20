# Function-based View
resource: https://www.django-rest-framework.org/api-guide/views/#function-based-views


# Class-based View
resource: https://www.django-rest-framework.org/api-guide/views/#class-based-views


|CRUD|Action|
|--:|:--|
|C|Create|
|R|Read or Retrieve|
|U|Update|
|D|Delete or Destroy|

## Read and Create a List of Items

### models.py
```python
from django.db import models


class Book(models.Model):  # not BookModel
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=500)
```

### settings.py
```python
INSTALLED_APPS = [
    '<app_name>.apps.<app_name in title case>Config',
    ...
]
```

```shell
python manage.py makemigrations
python manage.py migrate
```

### serializers
Create a `serializers.py` file in your app directory.

```python
from rest_framework import serializers
from <app_name>.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']
```

`IMPORTANT` Do not forget to look the resource!  
https://www.django-rest-framework.org/tutorial/quickstart/#serializers

### views.py
```python
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookListAPIView(APIView):
    def get(self, request:Request) -> Response:
        s = BookSerializer(instance=Book.objects.all(), many=True)
        return Response(s.data)

    def post(self, request:Request) -> Response:
        s = BookSerializer(data=request.data)
        if s.is_valid():
            s.save()
            # since, the serializer did the save method, it does have the id and returns that!!
            return Response(s.data, status=status.HTTP_201_CREATED)
            # good habit => status=201 means that object has been saved in the database

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
```

`IMPORTANT` Learn how to customize the `get_exception_handler` method in `APIView` class. Look at [Exceptions](exceptions.md) 

`IMPORTANT` Do not forget to look the resource!  
https://www.django-rest-framework.org/tutorial/quickstart/#views

### urls.py
```python
from django.contrib import admin
from django.urls import path

from tutorial.views import BookListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("book/", BookListAPIView.as_view()),
]
```

## Read and Update an Item

### views.py
```python
from django.http.response import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookDetailAPIView(APIView):
    def _get_object_or_404(self, pk) -> Book:
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book Not Found")
            # return Response(
            #     {"error": "Book Not Found"}, status=status.HTTP_404_NOT_FOUND
            # )

        return book

    def _update_book(self, pk, partial=False):
        s = BookSerializer(instance=self._get_object_or_404(pk), data=self.request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
            # since, a new item has not been created and just got updated, we shall send the response with status of 200

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        s = BookSerializer(instance=self._get_object_or_404(pk))
        return Response(s.data)

    def put(self, request, pk):
        return self._update_book(pk)

    def patch(self, request, pk):
        return self._update_book(pk, partial=True)

    def delete(self, request, pk):
        book = self._get_object_or_404(pk)
        book.delete()
        return Response()  # default 200
```

### urls.py
```python
from django.contrib import admin
from django.urls import path

from tutorial.views import BookDetailAPIView, BookListAPIView, hello


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("book/", BookListAPIView.as_view()),
    path("book/<int:pk>/", BookDetailAPIView.as_view()),
]
```
