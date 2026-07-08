# Django REST Framework (DRF)

## Django
<!-- link to the Django folder -->

## REST
REST is `design style` for writing `API`s.

## Framework
<!-- link to the Django folder -->

## Application Programming Interface (API)
- API is a service which programmers are the consumers and can use a service in their codes.
- An API can build a bridge between two services to work alongside.
- `Kavenegar` is an API example. This Iranian SMS-API provides the infrastructure for sending SMS through programming scripts.
- `Single Sign-On (SSO)` service is another example which can be provided by Google.
- The above mentioned services can be utilized in a programmer script

### Microservices
if APIs are micro

### Distributed services
if APIs are macro

## Design Style
my questions are:
- what is a design style?
- name some other design styles. Are they still popular or not?
- what technologies are they based on?
- time when they are introduced? Are they retired?
- Which field is that design style popular?

### SOAP
before REST, on HTTP and XML

### RPC and gRPC
on HTTP and popular for microservices
is the best for working between services, does not have the overhead of the REST

### REST
on HTTP with respect to HTTP methods and status
using XML and json, which json became more popular due to dictionary data structure in python and J-object in JavaScript. another reason is that the json is lighter.
* what is REST overhead ???

|Method|Usage as per REST|
|:--:|:--:|
|GET|read a list|
|GET|read an item|
|POST|create a list|
|POST|create an item|
|PUT|update whole|
|PATCH|update parts|
|DELETE|delete an item|
|DELETE|do not delete a list|

We can user the GET method to delete an item, but this is against what REST says. So, in code review, there shall be a hint indicating to follow the REST style.

## DRF vs Django
|DRF|Django|
|--:|:--|
|no page rendering||
|serializer||
|document||
|pagination||
|API Authentication (CSRF exempt by default)||

Browseable view looks like a playground to explore the API. It is useful to test the API. This feature can be disabled in the settings.py file.

Djnago returns an HttpResponse
DRF returns a Response, which is inherited from the HttpResponse.

DRF has changed the Django dispatcher. It will perform some actions before and after the dispatcher.

DRF has defined an `OPTION` method.

Django has Forms
DRF has Serializers

## Useful Links
https://restfulapi.net/  
https://www.django-rest-framework.org/