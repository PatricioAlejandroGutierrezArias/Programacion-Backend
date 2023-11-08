from django.shortcuts import render
from proyecto_4_app.models import Empleados

# Create your views here.
def listaempleados(request):
    emplea = Empleados.objects.all()
    data = {'emple': emplea}
    return render(request, 'empleados.html',data)