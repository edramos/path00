from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.toSignup, name='signupPage'),
    url(r'^login/$', views.toLogin, name='loginPage'),
    url(r'^signup/add$', views.addUser, name='signup'),
    url(r'^dashboard/$', views.login, name='login'),
    url(r'^dashboard/$', views.toDashboard, name='dashboardPage'),
    
]
