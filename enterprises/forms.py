from django import forms
from .models import Enterprise

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['id', 'name', 'description']