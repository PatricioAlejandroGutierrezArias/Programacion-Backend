from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = forms.registros(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error en el formulario')
    data = {'formss': form }
    return render(request, 'registro.html',data)

def eliminar(request, id):
    proye = Proyecto.objects.get(id=id)
    proye.delete()
    return redirect('/proyecto')

def modificar(request, id):
    proye = Proyecto.objects.get(id=id)
    form = forms.registros(instance=proye)
    if (request.method == 'POST'):
        form = forms.registros(request.POST, instance=proye)
    
        if form.is_valid():
            form.save()
        return index(request)
    
    data = {'formss':form}
    return render(request, 'registro.html', data)
    