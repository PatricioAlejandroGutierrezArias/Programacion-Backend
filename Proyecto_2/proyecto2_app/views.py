from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto2_app/index.html')

def Electronica(request):
    data = {"titulo" : "Electronica",
            "producto1" : "Reloj Inteligente",
            "producto2" : "Tester Digital",
            "producto3" : "Parlante BLuetooth",
            "foto1": "electronica1.jpg",
            "foto2": "electronica2.jpg",
            "foto3": "electronica3.jpg"}
    return render(request, 'proyecto2_app/producto.html', data)

def Ropa(request):
    data = {"titulo" : "Ropa",
            "producto1" : "Camisa",
            "producto2" : "Poleron",
            "producto3" : "Parka",
            "foto1": "ropa1.jpg",
            "foto2": "ropa2.jpg",
            "foto3": "ropa3.jpg"}
    return render(request, 'proyecto2_app/producto.html', data)

def Juguete(request):
    data = {"titulo" : "Juguete",
            "producto1" : "Autos",
            "producto2" : "Juego Didactico",
            "producto3" : "Muñeca Pepona",
            "foto1": "juguete1.jpg",
            "foto2": "juguete2.jpg",
            "foto3": "juguete3.jpg"}
    return render(request, 'proyecto2_app/producto.html', data)


