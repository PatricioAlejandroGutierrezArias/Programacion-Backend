from typing import Any
from django import forms
from . import models
from django.core import validators

class ParticipantesForm(forms.ModelForm):
     ESTADOS = [
        ('reservado', 'Reservado'),
        ('completada', 'Completada'),
        ('anulada', 'Anulada'),
        ('no asisten', 'No Asisten')]
     
     nombre = forms.CharField(label='Nombre', max_length=80, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     telefono = forms.IntegerField(label='Telefono', required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))   
     fecha_inscripcion = forms.DateField(label='Fecha de Inscripcion', required=True, widget=forms.DateInput(attrs={'class':'form-control'}))   
     hora_inscripcion = forms.TimeField(label='Hora de Inscripcion', required=True, widget=forms.TimeInput(attrs={'class':'form-control'})) 
     institucion = forms.ModelChoiceField(label='Institucion', queryset=models.Instituciones.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'})) 
     estado = forms.ChoiceField(label='Estado', choices=ESTADOS, required=True, widget=forms.Select(attrs={'class':'form-control'}))  
     observaciones = forms.CharField(label='Observaciones', max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))  
     
     class Meta:
         model = models.Participantes
         fields = ['nombre', 'telefono', 'fecha_inscripcion', 'hora_inscripcion', 'institucion', 'estado', 'observaciones']
        
     
class InstitucionesForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = models.Instituciones
        fields = ['nombre']