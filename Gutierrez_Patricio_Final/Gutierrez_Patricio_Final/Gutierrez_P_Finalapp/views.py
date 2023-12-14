from django.shortcuts import render

from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def registroparticipantes(request):
    form = forms.ParticipantesForm()
    if request.method == 'POST':
        form = forms.ParticipantesForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('Error en el formulario')
    data = {'formss': form}
    return render(request,'registroparticipantes.html',data)

def registroinstituciones(request):
    form = forms.InstitucionesForm()
    if request.method == 'POST':
        form = forms.InstitucionesForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('Error en el formulario')
    data = {'formss': form}
    return render(request,'registroinstituciones.html',data)