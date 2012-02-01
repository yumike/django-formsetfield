from django import forms
from .widgets import FormSetWidget


class FormSetField(forms.Field):

    widget = FormSetWidget

    def __init__(self, formset_class, template=None, *args, **kwargs):
        self.formset_class = formset_class
        self.template = template or 'formsetfield/formsetfield.html'
        super(FormSetField, self).__init__(*args, **kwargs)

    def validate(self, value):
        if not value.is_valid():
            raise forms.ValidationError(self.error_messages['invalid'])

    def clean(self, value):
        return super(FormSetField, self).clean(value).cleaned_data

    def widget_attrs(self, widget):
        return {'formset_class': self.formset_class, 'template': self.template}
