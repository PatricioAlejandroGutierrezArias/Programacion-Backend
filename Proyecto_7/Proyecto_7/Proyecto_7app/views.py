from django.http import JsonResponse
from django.shortcuts import render
from .models import Empleados

# Create your views here.
def empleadosView(request):
    emp = {
        'id' : 123,
        'nombre' : 'Juanito',
        'email' : 'juancho@gmail.com',
        'sueldo' : '500000000'
    }
    return JsonResponse(emp)

def empleadosView_DB(request):
    emple = Empleados.objects.all()
    data = {'emplea' : list(emple.values('nombre','sueldo'))}
    return JsonResponse(data)