from django.conf.urls import url
from locations.views import ListLocationView, CreateLocationView,\
    UpdateLocationView

urlpatterns = [
    url(r'^locations/$', ListLocationView.as_view(), name='locationsList'),
    url(r'^locations/add/$', CreateLocationView.as_view(), name='createLocation'),
    url(r'^locations/update/(?P<pk>\d+)$', UpdateLocationView.as_view(), name='updateLocation')
]