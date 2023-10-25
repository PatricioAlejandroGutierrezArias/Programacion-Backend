from django.shortcuts import render
from gestion_app.models import Productos

# Create your views here.

def busqueda(request):
    return render(request, "busqueda.html")

def busca(request):
    if request.GET ["prd"]:
        produc = request.GET["prd"]
        produ = Productos.objects.filter(nombre__icontains=produc)
        return render(request, "resultado.html", {"productos":produ, "query":produc})
    
    else: 
        mensaje = "No has introducido nada" 
        return render(request, "resultado.html", {"query":mensaje})
        
    