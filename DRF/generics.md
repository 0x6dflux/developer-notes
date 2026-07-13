# Implement CRUD Using Generics
Look at `models.py`, `settings.py`, and `serializers.py` in [APIView](/DRF/apiview.md) file.

## Read and Create a List of Items

### views.py
```python
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookListAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        s = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(s.data)

    def post(self, request):
        s = self.get_serializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
            # good habit => status=201 means that object has been saved in the database

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
```

```python
# even more concise
# the ListCreateAPIView inherits from 
# mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView
# which shall be used next to each others
# the mixins use some methods that are defined in the GenericAPIView class

from rest_framework.generics import ListCreateAPIView

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## Read and Update an Item

### views.py
```python
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookDetailAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = "pk", this is the default
    lookup_url_kwarg = "pk"

    def _update_book(self, pk, partial=False):
        s = self.get_serializer(
            instance=self.get_object(),
            data=self.request.data,
            partial=partial,
        )
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
            # since, a new item has not been created and just got updated, we shall send the response with status of 200

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        s = self.get_serializer(instance=self.get_object())
        return Response(s.data)

    def put(self, request, pk):
        return self._update_book(pk)

    def patch(self, request, pk):
        return self._update_book(pk, partial=True)

    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response()  # default 200
```

```python
# even more concise

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = "pk", this is the default
    lookup_url_kwarg = "pk"
```


## Add a Filter
Suppose you want to show books that contain an specific word in their title. This specific word comes from a query string in the request. 

To implement this feature, there is a function in `GenericAPIView` titled `get_queryset`, which is responsible to update the `queryset` on every request. All we have to do, is to modify this function.

```python
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView

from tutorial.models import Book
from tutorial.serializers import BookSerializer


class BookListAPIView(ListCreateAPIView):
    # model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        conditions = Q()

        allowed_fields = {f.name for f in self.queryset.model._meta.get_fields()}
        # allowed_fields = {f.name for f in self.model._meta.get_fields()}
        # the above definition requires, model = Book

        for field, value in self.reques.GET.items():
            if field not in allowed_fields:
                continue

            conditions = conditions & Q(**{field+'__icontains': value})
        
        return queryset.filter(conditions)
```