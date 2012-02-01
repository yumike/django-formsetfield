Django FormSetField
===================

Django's form wizard allows you to have only one form or one formset
(since 1.4) per step. Using `django-formfield`_ you can have more forms per
step. Using this app you can have more `formsets`_ per step.

Or maybe you will find other use cases for it :)

Installation
------------

1. Install ``django-formsetfield`` with pip::

       $ pip install django-formsetfield

2. Add ``formsetfield`` to ``INSTALLED_APPS``.

Usage example
-------------

::

    from django import forms
    from formsetfield.fields import FormSetField


    class AdultForm(forms.Form):

        fullname = forms.CharField()
        passport = forms.CharField()


    class ChildForm(forms.Form):

        fullname = forms.CharField()
        birth_certificate = forms.CharField()


    class PassengersForm(forms.Form):

        adults = FormSetField(formset_factory(AdultForm))
        children = FormSetField(formset_factory(ChildForm))

Contributing
------------

Feel free to fork, send pull requests or report bugs and issues on `github`_.

.. _django-formfield: https://github.com/josesoa/django-formfield/
.. _formsets: http://django.me/formsets
.. _github: https://github.com/yumike/django-formsetfield/
