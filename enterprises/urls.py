from django.conf.urls import url
from enterprises.views import EnterpriseUpdate

urlpatterns = [
    url(r'^enterprise/edit/(?P<pk>\d+)$', EnterpriseUpdate.as_view(), name="enterpriseUpdate")
]