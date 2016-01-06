from django.views.generic.list import ListView

from locations.models import Location

class ListLocationView(ListView):
    model = Location
    template_name = "locations/location.html"
    
    def get_queryset(self):
        return Location.objects.filter(state='enabled', enterprise_id=self.request.session['idEnterprise'])
    
