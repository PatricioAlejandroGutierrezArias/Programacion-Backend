from django.shortcuts import redirect, render
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def registroparticipantes(request):
    form = forms.ParticipantesForm()
    if request.method == 'POST':
        form = forms.ParticipantesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registroparticipantes')
        else:
            print('Error en el formulario')
    data = {'formss': form}
    return render(request,'registroparticipantes.html',data)

def registroinstituciones(request):
    form = forms.InstitucionesForm()
    if request.method == 'POST':
        form = forms.InstitucionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registroinstituciones')
        else:
            print('Error en el formulario')
    data = {'formss': form}
    return render(request,'registroinstituciones.html',data)

class AutorProyectoDetail(APIView):
    def get(self, request, format=None):
        autor = AutorProyecto.objects.first()
        data = {
            "id": autor.id,
            "nombre": autor.nombre,
            "carrera": autor.carrera,
            "correo": autor.correo,
        }
        return Response(data)
    
 #Class Based Views para el Modelo Inscritos
 
class participantes_list(APIView):
    def get(self, request, format=None):
        participantes = Participantes.objects.all()
        serial = ParticipantesSerializer(participantes, many=True)
        return Response(serial.data)
    
    def post(self, request, format=None):
        serial = ParticipantesSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
class participantes_detail(APIView):
    def get_object(self, id):
        try:
            return Participantes.objects.get(pk=id)
        except Participantes.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        participantes = self.get_object(id)
        serial = ParticipantesSerializer(participantes)
        return Response(serial.data)
    
    def put(self, request, id, format=None):
        participantes = self.get_object(id)
        serial = ParticipantesSerializer(participantes, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id, format=None):
        participantes = self.get_object(id)
        participantes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        
 #Class Funcion based Views para el Modelo Instituciones
 
@api_view(['GET','POST'])
def instituciones_list(request):
    if request.method == 'GET':
        instituciones = Instituciones.objects.all()
        serial = InstitucionesSerializer(instituciones, many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = InstitucionesSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def instituciones_detail(request, id):
    try:
        instituciones = Instituciones.objects.get(pk=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionesSerializer(instituciones)
        return Response(serial.data)
    
    elif request.method == 'PUT':
        serial = InstitucionesSerializer(instituciones, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        instituciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)