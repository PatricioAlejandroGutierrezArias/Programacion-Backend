from typing import Any
from django import forms
from . import models
from django.core import validators

class registros(forms.ModelForm):
    ESTADOS = [
        ('reservado', 'Reservado'),
        ('completada', 'Completada'),
        ('anulada', 'Anulada'),
        ('no asisten', 'No Asisten')]
  
    nombre = forms.CharField(validators=[validators.MaxLengthValidator(80)])
    telefono = forms.IntegerField()
    fecha = forms.DateField()
    hora = forms.TimeField()
    cantidad_personas =forms.IntegerField(validators =[validators.MinValueValidator(1),validators.MaxValueValidator(20)])
    email = forms.EmailField(widget=forms.EmailInput)
    estado = forms.ChoiceField(widget=forms.Select, choices=ESTADOS)
    observacion = forms.CharField(required=False)
    
    class Meta:
        model = models.reservas
        fields = '__all__'
    
        
   
       