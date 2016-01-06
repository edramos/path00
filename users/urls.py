from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.toSignup, name='signupPage'),
    url(r'^login/$', views.toLogin, name='loginPage')
]
