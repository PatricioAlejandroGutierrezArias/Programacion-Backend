from django.http import HttpResponse 
import datetime

#aca se crea la vista

def saludo(request): #primera vista
    return HttpResponse("<h1>Hola a todos Bienvenidos a Django</h1>")   #devuelve un objeto de tipo HttpResponse


def adios(request): #segunda vista
    return HttpResponse("Adios a todos")   #devuelve un objeto de tipo HttpResponse

def chao2(request): #segunda vista
    docu="""
    <html>
        <body>
            <h1>Hola de Nuevo</h1>
        </body>
    </html>"""
    return HttpResponse(docu)   #devuelve un objeto de tipo HttpResponse

def horaactual(request):
    fecha_actual=datetime.datetime.now()
    docu="""
    <html>
        <body>
            <h1>La fecha y hora actual es: %s</h1>
        </body>
    </html>""" % fecha_actual
    return HttpResponse(docu) 
    
def calculo(request,anio):
    edad = 18
    periodo = anio - 2023
    edadfutura = edad + periodo
    docu="""
    <html>
        <body>
            <h1>En el año %s tendras %s años</h1>
        </body>
    </html>""" %(anio,edadfutura)
    return HttpResponse(docu)

def calcularedad(request,edad,anio):
    periodo = anio - 2023
    edadfutura = edad + periodo
    docu="""
    <html>
        <body>
            <h1>En el año %s tendras %s años</h1>
        </body>
    </html>""" %(anio,edadfutura)
    return HttpResponse(docu)