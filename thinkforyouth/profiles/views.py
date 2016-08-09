from allauth.account.views import SignupView
from django.urls import reverse_lazy


class RegistrationView(SignupView):
    success_url = reverse_lazy('pages:home')

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['test'] = 'Hello from custom view'
        return context
