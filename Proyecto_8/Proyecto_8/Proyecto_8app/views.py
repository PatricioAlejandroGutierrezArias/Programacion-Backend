from django.shortcuts import render
from .models import Estudiantes
from .serializers import EstudiantesSerializer
from rest_framework.response import Response
from rest_framework import status  
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST']) 
def estudiantes_list(request):
    if request.method == 'GET':
        estudi = Estudiantes.objects.all()
        serial = EstudiantesSerializer(estudi, many=True)
        return Response(serial.data)
    if request.method == 'POST':
        serial = EstudiantesSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Crear el update y el delete
@api_view(['GET', 'PUT', 'DELETE'])
def estudiantes_detail(request, pk):
    try:
        estudi = Estudiantes.objects.get(pk=pk)
    except Estudiantes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        estudi = Estudiantes.objects.filter(id=pk).first()
        serial = EstudiantesSerializer(estudi)
        return Response(serial.data)
    
    elif request.method == 'PUT':
        estudi = Estudiantes.objects.filter(id=pk).first()
        serial = EstudiantesSerializer(estudi, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        estudi = Estudiantes.objects.filter(id=pk).first()
        estudi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)