from django import forms
from jobslip.models import Customer
from django.db.models import fields
from django.db.models.base import Model


class CustomerForms(forms.ModelForm):
    class Meta:
        model= Customer
        fields = '__all__'