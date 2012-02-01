from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class FormSetWidget(forms.Widget):

    def render(self, name, value, attrs=None):
        if value is None:
            value = self.attrs['formset_class'](prefix=name)
        return render_to_string(self.attrs['template'], {'formset': value})

    def value_from_datadict(self, data, files, name):
        return self.attrs['formset_class'](data, files, prefix=name)
