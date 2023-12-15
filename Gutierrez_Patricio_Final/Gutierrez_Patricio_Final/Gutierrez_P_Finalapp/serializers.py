from rest_framework import serializers
from .models import *

class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = '__all__'
        
class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'
        
