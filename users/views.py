from django.shortcuts import render
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from users.forms import UserForm
from enterprises.models import Enterprise
from locations.models import Location
from users.models import User, Profile


def toSignup(request):
    return render(request, 'users/signup.html')

def toLogin(request):
    return render(request, 'users/login.html')

def addUser(request):
    form = UserForm(request.POST)
    
    if form.is_valid():
        try:
            with transaction.atomic():
                enterprise = Enterprise()
                enterprise.save()
                request.session['idEnterprise'] = enterprise.id;
                
                location= Location(enterprise=enterprise, lat=0, lng=0, name='Main Office')
                location.save()
                
                user = User(location = location, email=form.cleaned_data['email'], 
                        password=form.cleaned_data['password'])
                user.save()
                request.session['idUser'] = user.id;
                
                profile = Profile(user = user, role="Administrator")
                profile.save()
                
                return render(request, 'users/dashboard.html')
                
        except Exception as e:
            print(e)
            messages.error(request, 'Sorry, Internal Error')
                
    else:
        messages.error(request, 'Please fill the form')
        return HttpResponseRedirect('/signup')

    
def login(request):
    form = UserForm(request.POST)
    
    if form.is_valid():
        try:
            u = User.objects.get(email=form.cleaned_data['email'], 
                             password=form.cleaned_data['password'])
            request.session['idUser'] = u.id
            
            l = Location.objects.get(user__id=request.session['idUser'])
            e = Enterprise.objects.get(location__id=l.id)
            request.session['idEnterprise'] = e.id
            
            return render(request, 'users/dashboard.html')
        
        except ObjectDoesNotExist:
            messages.error(request, 'Incorrect username or password.')
            return HttpResponseRedirect('/login')
        
    else:
        messages.error(request, 'Please fill the form')
        return HttpResponseRedirect('/login')
    
#be careful, it needs to change because it'll be easy to hack
def toDashboard(request):
    return render(request, 'users/dashboard.html')


#Left Menu Links
def toLocation(request):
    return render(request, 'users/location.html')

def toEmployee(request):
    return render(request, 'users/employee.html')
        
        
        
        
        
        
        
        
        
        
