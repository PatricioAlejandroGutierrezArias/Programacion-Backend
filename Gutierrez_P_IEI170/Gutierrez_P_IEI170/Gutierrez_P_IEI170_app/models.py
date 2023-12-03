from django.db import models

# Create your models here.
class reservas(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()
    email = models.EmailField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=200 , null=True)
    
    class meta:
        db_table = 'reservas'
