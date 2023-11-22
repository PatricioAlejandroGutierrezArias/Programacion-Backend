from typing import Any
from django import forms
from django.core import validators

class registros(forms.Form):
    fechaInicio = forms.DateField()
    fechaTermino = forms.DateField()
    nombre = forms.CharField()
    responsable= forms.CharField()
    prioridad = forms.IntegerField()
    
    class Meta:
        db_table = 'proyecto'
   
    fechaInicio.widget.attrs['class'] = 'form-control'
    fechaTermino.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    responsable.widget.attrs['class'] = 'form-control'
    prioridad.widget.attrs['class'] = 'form-control'