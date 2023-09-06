from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto2_app/index.html')

def producto(request):
    data = {"titulo" : "Electronica"}
    return render(request, 'proyecto2_app/producto.html', data)