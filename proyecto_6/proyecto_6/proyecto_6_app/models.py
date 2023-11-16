from django.db import models

# Create your models here.
class Proyecto(models.Model):
    FechaInicido = models.DateField() 
    FechaTermino = models.DateField() 
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()
    
    class Meta:
        db_table = 'proyecto'
