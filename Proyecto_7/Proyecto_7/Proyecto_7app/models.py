from django.db import models

# Create your models here.
class Empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    sueldo = models.DecimalField(max_digits=6, decimal_places=2)
    