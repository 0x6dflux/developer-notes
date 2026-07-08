# Setup
Resource: https://www.django-rest-framework.org/tutorial/quickstart/

## Project Setup
```shell
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv .venv --prompt <your venv name>
source .venv/bin/activate

# Install Django and Django REST framework into the virtual environment
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

`SHORTCUT` I have defined multiple functions in my shell to perform the above commands.
```shell
drfsp <project_name>
# Note that this command uses the `config` name.

drfsa <app_name>
# Note that this command will create the below files:
# - urls.py
# - serializers.py
# - views module
# - models module
# Do we need templates?? if yes, uncomment it in the shell!!

git add <all created folders and files>
git commit -m "Add django project and <app_name> app"
```

```shell
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Install requirements"
```

Modify the `TIME_ZONE = 'Asia/Tehran'` in the `settings.py`.

Add `'rest_framework'` to `INSTALLED_APPS`.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Quick Run
```python
# <app_name>/views.py

from rest_framework.request import Request
from rest_framework.response import Response


# Function-Based View (FBV)
from rest_framework.decorators import api_view


@api_view(['GET'])  # or @api_view(), default method is 'GET'
def hello(request:Request) -> Response:
    return Response('HelloWorld')
    # return 'HelloWorld' will raise an error


# Class-Based View (CBV)
from rest_framework.views import APIView


class HelloAPIView(APIView):
    def get(self, request:Request) -> Response:
        return Response('HelloWorld')
```

```python
# urls.py
# add below codes

from <app_name>.views import hello


urlpatterns = [
    ...
    path('hello/', hello),
]
```

```shell
python manage.py runserver
```
Congratulations! Now, you can see the browseable view.


# Implement CRUD

## models.py
```python
from django.db import models


class Book(models.Model):  # not BookModel
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=500)
```

## settings.py
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

## serializers
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

## views.py
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

`IMPORTANT` Do not forget to look the resource!  
https://www.django-rest-framework.org/tutorial/quickstart/#views

## url.py
```python
from django.contrib import admin
from django.urls import path

from tutorial.views import BookListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("book/", BookListAPIView.as_view()),
]
```