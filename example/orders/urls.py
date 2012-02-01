from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from django.views.generic import FormView, TemplateView

from .views import PassengersFormView

reverse_lazy = lazy(reverse, str)

urlpatterns = patterns('',
    url(r'^$',
        PassengersFormView.as_view(success_url=reverse_lazy('orders_success')),
        name='orders_form'),
    url(r'^success/$',
        TemplateView.as_view(template_name='orders/success.html'),
        name='orders_success'),
)
