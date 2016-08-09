from django.conf.urls import url

from .views import RegistrationView

urlpatterns = [
    url(r'^signup/$', RegistrationView.as_view(), name = 'account_signup'),
]
