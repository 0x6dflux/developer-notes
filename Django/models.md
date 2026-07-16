


## CharField
resource: https://docs.djangoproject.com/en/6.0/ref/models/fields/#charfield

### max_length
The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation using [MaxLengthValidator](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.MaxLengthValidator). It’s required for all database backends included with Django except PostgreSQL and SQLite, which supports unlimited VARCHAR columns.

`NOTE` If you are writing an application that must be portable to multiple database backends, you should be aware that there are restrictions on max_length for some backends. Refer to the [database backend notes](https://docs.djangoproject.com/en/6.0/ref/databases/) for details.