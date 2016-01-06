from django import forms
from .models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'telephone', 'role']
        