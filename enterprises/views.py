from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from .models import Enterprise
from enterprises.forms import EnterpriseForm

class EnterpriseUpdate(UpdateView):    
    model = Enterprise
    template_name = "enterprises/enterprise.html"
    form_class = EnterpriseForm
    
    def get_success_url(self):
        return reverse('enterpriseUpdate', kwargs={'pk': self.kwargs['pk']})
    