from typing import Any
from django import forms
from . import models
from django.core import validators

class ParticipantesForm(forms.ModelForm):
     ESTADOS = [
         ('---------', '---------'),
        ('reservado', 'Reservado'),
        ('completada', 'Completada'),
        ('anulada', 'Anulada'),
        ('no asisten', 'No Asisten')]
     
     nombre = forms.CharField(label='Nombre', validators=[validators.MaxLengthValidator(80)], required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     telefono = forms.IntegerField(label='Teléfono', required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))   
     fecha_inscripcion = forms.DateField(label='Fecha de Inscripción', required=True, widget=forms.DateInput(attrs={'class':'form-control'}))   
     hora_inscripcion = forms.TimeField(label='Hora de Inscripción', required=True, widget=forms.TimeInput(attrs={'class':'form-control'})) 
     institucion = forms.ModelChoiceField(label='Institución', queryset=models.Instituciones.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'})) 
     estado = forms.ChoiceField(label='Estado', choices=ESTADOS, required=True, widget=forms.Select(attrs={'class':'form-control'}))  
     observaciones = forms.CharField(label='Observaciones', validators=[validators.MaxLengthValidator(100)], required=True, widget=forms.TextInput(attrs={'class':'form-control'}))  
     
     class Meta:
         model = models.Participantes
         fields = ['nombre', 'telefono', 'fecha_inscripcion', 'hora_inscripcion', 'institucion', 'estado', 'observaciones']
         
     def clean(self):
         cleaned_data = super().clean()
         nombre = cleaned_data.get('nombre')
         
        
         #verifica si ya existe participante registrado mismo nombre 
         existe_participante = models.Participantes.objects.filter(nombre=nombre).exists()
        
         if existe_participante:
             raise forms.ValidationError('El participante ya esta registrado/a')
        
     
class InstitucionesForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = models.Instituciones
        fields = ['nombre']
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        
        #verifica si ya existe la institucion
        existe_institucion = models.Instituciones.objects.filter(nombre=nombre).exists()
        
        if existe_institucion:
            raise forms.ValidationError('La institución ya esta registrada')