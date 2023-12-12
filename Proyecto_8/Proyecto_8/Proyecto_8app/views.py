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