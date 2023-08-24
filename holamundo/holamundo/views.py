from django.http import HttpResponse

#aca se crea la vista

def saludo(request): #primera vista
    return HttpResponse("<h1>Hola a todos Bienvenidos a Django</h1>")   #devuelve un objeto de tipo HttpResponse

def adios(request): #segunda vista
    return HttpResponse("Adios a todos")   #devuelve un objeto de tipo HttpResponse