from django.shortcuts import render

# Create your views here.

def usotemplate(request):
    return render(request, 'templateapp1/plantilla.html')

def infousuario(request):
    data = {"ID": "123", "Nombre": "Clark kent", 
            "email": "superman@jl.org"}
    return render(request, 'templateapp1/plantilla.html',data)