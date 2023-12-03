from django.shortcuts import redirect, render
from Gutierrez_P_IEI170_app.models import reservas
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')  

def listadoreservas(request):
    reser = reservas.objects.all()
    data = {'reservas':reser}
    return render(request, 'reservas.html',data) 

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

def eliminar(request, id):
    reser = reservas.objects.get(id=id)
    reser.delete()
    return redirect('reservas')

def modificar(request, id):
    reser = reservas.objects.get(id=id)
    form = forms.registros(instance=reser)
    if (request.method == 'POST'):
        form = forms.registros(request.POST, instance=reser)
        
        if form.is_valid():
            form.save()
            return redirect('reservas')
        else:
            print('Error en el Formulario')
    data = {'formss':form}
    return render(request, 'registro.html',data)
