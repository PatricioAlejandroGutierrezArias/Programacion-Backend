from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    nota =models.DecimalField(max_digits=2, decimal_places=1)
    

  