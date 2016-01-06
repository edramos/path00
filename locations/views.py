from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView

from locations.models import Location


class ListLocationView(ListView):
    model = Location
    template_name = "locations/location.html"
    
    def get_queryset(self):
        return Location.objects.filter(state='enabled', enterprise_id=self.request.session['idEnterprise'])
    

class CreateLocationView(CreateView):
    model = Location
    fields = ['enterprise', 'name', 'address', 'city', 'usState', 'zipCode', 'lat', 'lng']
    template_name = "locations/addLocation.html"
        
    def form_valid(self, form):
        print("To valid")
        return CreateView.form_valid(self, form)
    
    def form_invalid(self, form):
        print("invalid: ", form.instance)
        return CreateView.form_invalid(self, form)
    
    def get_success_url(self):
        return reverse('locationsList')



class UpdateLocationView(UpdateView):
    model = Location
    fields = ['name', 'address', 'city', 'usState', 'zipCode', 'lat', 'lng']
    template_name = "locations/updateLocation.html"
    
    def form_invalid(self, form):
        print("invalid: ", form.instance.city, form.instance.name, form.instance.address , form.instance.usState, form.instance.zipCode, form.instance.lat, form.instance.lng)
        return UpdateView.form_invalid(self, form)
    
    def get_success_url(self):
        return reverse('locationsList')
    
    
    
    
