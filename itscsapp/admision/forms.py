from django.forms import ModelForm
from .models import AdmisionCarrer, AdmisionEvent
from django import forms


class AdmisionCarrerForm(ModelForm):
    class Meta:
        model = AdmisionCarrer
        fields = ['first_name', 'last_name', 'phone', 'email', 'carrer']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class AdmisionEventForm(ModelForm):
    class Meta:
        model = AdmisionEvent
        fields = ['first_name', 'last_name', 'phone', 'email', 'event']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
