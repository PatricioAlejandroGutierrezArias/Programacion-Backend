from django import forms
from django.core import validators

class registroempleados(forms.Form):
    ESTADOS = [
        {'activos','ACTIVOS'},
        {'inactivos','INACTIVOS'},
        {'bloqueado','BLOQUEADOS'}]
    
    nombre= forms.CharField(validators =[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    email= forms.EmailField(widget=forms.EmailInput)
    fono = forms.IntegerField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    estados = forms.ChoiceField(widget=forms.Select, choices=ESTADOS)
    class Meta:
        db_table = 'empleados'
        
    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    fono.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
    estados.widget.attrs['class'] = 'form-select'
    