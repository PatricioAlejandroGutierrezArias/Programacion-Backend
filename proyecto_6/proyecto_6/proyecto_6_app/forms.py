from typing import Any
from django import forms
from . import models 
from django.core import validators

class registros(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = '__all__'
        