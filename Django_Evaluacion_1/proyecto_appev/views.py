from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto_appev/index.html')

def Viento(request):
    data = {    "titulo": "Viento",
                "producto1" :"Flauta",
                "producto2" :"Tuba",
                "producto3" :"Clarinete",
                "foto1":"viento1.jpg",
                "foto2":"viento2.jpg",
                "foto3":"viento3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Cuerda(request):
    data = {    "titulo": "Cuerda",
                "producto1" :"Guitarra",
                "producto2" :"Violin",
                "producto3" :"VIolonchelo",
                "foto1":"cuerda1.jpg",
                "foto2":"cuerda2.jpg",
                "foto3":"cuerda3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Percusion(request):
    data = {    "titulo": "Percusion",
                "producto1" :"Bateria",
                "producto2" :"Tambor",
                "producto3" :"Pandereta",
                "foto1":"percusion1.jpg",
                "foto2":"percusion2.jpg",
                "foto3":"percusion3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Usuario(request):
    data = {    "Titulo": "Usuario",
                "nombre" :"Juan",
                "apellido" :"Perez",
                "email" :"",
                "telefono" :"",
                "foto1":"usuario1.jpg"
                }
    return render(request, 'proyecto_appev/usuario.html',data)

