from django.conf.urls import url
from locations.views import ListLocationView

urlpatterns = [
    url(r'^locations/$', ListLocationView.as_view(), name='locationsList'),
]