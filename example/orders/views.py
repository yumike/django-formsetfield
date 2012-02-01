from django.views.generic import FormView
from .forms import PassengersForm


class PassengersFormView(FormView):

    form_class = PassengersForm
    template_name = 'orders/form.html'

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
