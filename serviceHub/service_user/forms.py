from django.forms import ModelForm
from django import forms
from .models import service_offered



class MyServiceForm(ModelForm):
    class Meta:
        model = service_offered
        fields = '__all__'
        widgets = {
          'service_description': forms.Textarea(attrs={'rows':10, 'cols':109}),
        }