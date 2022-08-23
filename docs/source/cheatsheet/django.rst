Django
======

Project 
-------

Creating a project
++++++++++++++++++

.. code ::

    $ django-admin startproject mysites

Creating an app
+++++++++++++++

.. code ::

    $ python manage.py startapp polls


Running Development server
++++++++++++++++++++++++++

.. code ::

    $ python manage.py runserver

Models
------

Creating Models
+++++++++++++++

.. code ::

    from django.db import models


    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')


    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

Migrations 
++++++++++

.. code ::

    $ python manage.py makemigrations polls
    $ python manage.py migrate

Fields 
++++++

* Documentation: https://docs.djangoproject.com/en/4.1/ref/models/fields/

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - Integer
     - :code:`models.IntegerField()`
   * - Float
     - :code:`models.FloatField()`
   * - Char
     - :code:`models.CharField(max_length=None)`
   * - Text
     - :code:`models.TextField()`
   * - File
     - :code:`models.FileField(upload_to='uploads/')`
   * - Email
     - :code:`models.EmailField()`
   * - Foreign Key 
     - :code:`models.ForeignKey({model_name}, on_delete=models.CASCADE)`


Views
-----

Creating a View
+++++++++++++++


.. code ::

    # views.py
    from django.views.generic import ListView
    from polls.models import Question

    class QuestionListView(ListView):
        model = Question


.. code ::

    # urls.py
    from django.urls import path
    from polls.views import QuestionListView

    urlpatterns = [
        path('questions/', QuestionListView.as_view()),
    ]

Class-based Views
+++++++++++++++++

* Inspector: https://ccbv.co.uk

.. list-table::
   :widths: 25 25 50
   :header-rows: 0


   * - Generic 
     - :code:`View`
     - :code:`django.views`
   * - Template
     - :code:`TemplateView`
     - :code:`django.views.generic`
   * - List
     - :code:`ListView`
     - :code:`django.views.generic`
   * - Detail
     - :code:`DetailView`
     - :code:`django.views.generic`
   * - Form
     - :code:`FormView`
     - :code:`django.views.generic.edit`
   * - Create
     - :code:`CreateView`
     - :code:`django.views.generic.edit`
   * - Delete
     - :code:`DeleteView`
     - :code:`django.views.generic.edit`
   * - Update
     - :code:`UpdateView`
     - :code:`django.views.generic.edit`


Administration
--------------

Creating an admin user
++++++++++++++++++++++

.. code ::

    $ python manage.py createsuperuser

Creating a View 
+++++++++++++++

.. code ::

    from django.contrib import admin
    from .models import Question

    admin.site.register(Question)


