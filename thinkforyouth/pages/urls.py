from django.conf.urls import url

from . import views

app_name = 'pages'

urlpatterns = [
    url('^$', views.home, name = 'home')
]
