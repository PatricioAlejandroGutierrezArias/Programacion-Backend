from django.shortcuts import render
from proyecto_6_app.models import Proyecto
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoproyecto(request):
    proye = Proyecto.objects.all()
    data = {'proyecto':proye}
    return render(request, 'proyecto.html',data)

def registro(request):
    form = forms.registros() 
    data = {'formss': form }
    return render(request, 'registro.html',data)
    