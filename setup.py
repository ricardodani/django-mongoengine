#!/usr/bin/env python
# Copyright (c) 2010 Seth Buntin, seth@buntin.org

from setuptools import setup

setup(name='django-mongoengine',
      version=open('django_mongoengine/version.txt').read(),
      author="Seth Buntin",
      author_email="seth@buntin.org",
      url="http://github.com/sethtrain/django-mongoengin",
      description='MongoEngine bridge to Django',
      long_description=open('README.md').read(),
      package_dir={'djangomongokitlib':'django-mongokitlib'},
      packages=['django_mongoengine'],
      package_data={'django_mongoengine':['version.txt']},
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities']
)