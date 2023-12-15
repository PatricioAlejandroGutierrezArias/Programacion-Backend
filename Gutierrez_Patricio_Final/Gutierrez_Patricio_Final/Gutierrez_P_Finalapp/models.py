from django.db import models

# Create your models here.

class Participantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField()
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "Participantes"
        
class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "Instituciones"
        
class AutorProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    carrera = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "AutorProyecto"
    
        