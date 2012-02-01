from django import forms
from django.forms.formsets import formset_factory

from formsetfield.fields import FormSetField


class AdultForm(forms.Form):

    fullname = forms.CharField()
    passport = forms.CharField()


class ChildForm(forms.Form):

    fullname = forms.CharField()
    birth_certificate = forms.CharField()


class PassengersForm(forms.Form):

    adults = FormSetField(formset_factory(AdultForm, extra=2))
    children = FormSetField(formset_factory(ChildForm, extra=2))
