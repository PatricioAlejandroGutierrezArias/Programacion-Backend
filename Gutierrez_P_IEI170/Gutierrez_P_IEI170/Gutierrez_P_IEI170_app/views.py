from django.shortcuts import render,redirect
from Gutierrez_P_IEI170_app.models import reservas
from . import forms


# Create your views here.


def index(request):
    user_data = {
        "nombre": "Patricio Alejandro",
        "apellido": "Gutiérrez Arias",
        "telefono": "+569 12345678",
        "email": "patricio.gutierrez@inacapmail.cl"
        
    }
    return render(request, 'index.html', {'user_data': user_data})


def listadoresevas(request):
    reser = reservas.objects.all()
    data = {'reservas':reser}
    return render(request, 'reservas.html', data)

def registro(request):
    form = forms.registros()
    if request.method == 'POST':
        form = forms.registros(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('Error en el Formulario')
    data = {'formss':form}
    return render(request, 'registro.html',data) 

def eliminar(request, ID):
    reser = reservas.objects.get(ID=ID)
    reser.delete()
    return redirect('/reservas')

def modificar(request, ID):
    proye = reservas.objects.get(ID=ID)
    form = forms.registros(instance=proye)
    if (request.method == 'POST'):
        form = forms.registros(request.POST, instance=proye)
    
        if form.is_valid():
            form.save()
        return index(request)
    
    data = {'formss':form}
    return render(request, 'registro.html', data)




