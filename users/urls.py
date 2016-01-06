from django.conf.urls import url
from . import views
from users.views import EditProfile

urlpatterns = [
    url(r'^signup/$', views.toSignup, name='signupPage'),
    url(r'^login/$', views.toLogin, name='loginPage'),
    url(r'^signup/add$', views.addUser, name='signup'),
    url(r'^dashboard/$', views.login, name='login'),
    url(r'^dashboard/$', views.toDashboard, name='dashboardPage'),
    url(r'^profile/update/(?P<pk>\d+)$', EditProfile.as_view(), name='updateProfile'),
    url(r'^logout/$', views.toLogout, name='logoutPage'),
    url(r'^employees/$', views.toEmployee, name='employeePage')
]
