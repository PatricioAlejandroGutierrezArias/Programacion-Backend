from django.shortcuts import render

# Create your views here.

def busqueda(request):
    return render(request, "busqueda.html")
