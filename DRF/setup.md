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
