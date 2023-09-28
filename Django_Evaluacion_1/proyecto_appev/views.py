from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto_appev/index.html')

def Viento(request):
    data = {    "titulo": "Viento",
                "categoria" :"viento",
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
                "categoria" :"cuerda",
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
                "categoria" :"percusion",
                "producto1" :"Bateria",
                "producto2" :"Tambor",
                "producto3" :"Pandereta",
                "foto1":"percusion1.jpg",
                "foto2":"percusion2.jpg",
                "foto3":"percusion3.jpg"
                }
    return render(request, 'proyecto_appev/producto.html',data)

def Usuario(request):
    data = {    "titulo": "Usuario",
                "ID" :"123",
                "nombre" :"Patricio Alejandro",
                "apellido" :"Gutiérrez Arias",
                "email" :"patricio.gutierrez@inacapmail.cl",
                "foto1":"usuario1.jpg"
                }
    return render(request, 'proyecto_appev/usuario.html',data)



def Descripcion(request,categoria,producto):
    descripciones = {
        "viento":{"Flauta":"La flauta y la ...... ",
                     "Tuba":"La tuba y la ...... ",
                     "Clarinete":"El clarinete y la ...... "},
        "cuerda":{  "Guitarra":"La guitarra y la ...... ",
                    "Violin":"El violin y la ...... ",
                    "VIolonchelo":"El violonchelo y la ...... "},
        "percusion":{   "Bateria":"La bateria y la ...... ",
                        "Tambor":"El tambor y la ...... ",
                        "Pandereta":"La pandereta y la ...... "}
    }
    
    descripcion = descripciones.get(categoria, {}).get(producto, "descripcion no encontrada")

    
    data = {    "titulo": "Descripcion",
                "categoria" : categoria,
                "producto" : producto,
                "descripcion" : descripcion
                
                
                }
    return render(request, 'proyecto_appev/descripcion.html',data)