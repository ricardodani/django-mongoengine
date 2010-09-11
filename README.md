django-mongoengine
==================

django-mongoengine's aim is to provide various functionalities developers are accustomed to when using Django.
Currently the features on the radar are:

    1. Document signals (pre_save, post_save, pre_delete, post_delete)
    2. DocumentForms, similar to Django's ModelForms

Installation
------------

    $ pip install django-mongoengine

Testing
-------

Prerequisites

- Django
- MongoEngine
- Nose

To run tests:

    $ env DJANGO_SETTINGS_MODULE=django_mongoengine.test_settings nosetests
