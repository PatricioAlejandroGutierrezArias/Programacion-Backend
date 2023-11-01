from django.db import models

class Ciudad(models.Model):
    Id = models.AutoField(primary_key=True)  # Usamos AutoField para crear un campo autoincremental
    IdCiudad = models.IntegerField(unique=True)  # Hacemos que el segundo campo sea la clave primaria
    Nombre = models.TextField(max_length=50)
    
class Region(models.Model):
    Id = models.AutoField(primary_key=True)  # Usamos AutoField para crear un campo autoincremental
    IdRegion = models.IntegerField(unique=True)  
    Nombre = models.TextField( max_length=50)  

class Comuna(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdComuna = models.IntegerField(unique=True)  
    Nombre = models.CharField(max_length=50) 

class Ubicacion(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdUbicacion = models.IntegerField(unique=True)  
    Estanteria = models.CharField(max_length=50)  
    Nivel = models.CharField(max_length=50)  
    Segmento = models.CharField(max_length=50)  


class Estado(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdEstado = models.IntegerField( unique=True) 
    Nombre = models.CharField(max_length=50)  

   

class Rol(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdRol = models.IntegerField(unique=True)  
    Descripcion = models.CharField(max_length=50)  

    

class Tipo(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdTipo = models.IntegerField(unique=True)  
    Nombre = models.CharField(max_length=50)  
   

class Usuarioestado(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdEstado = models.IntegerField(unique=True)  
    Nombre = models.CharField(max_length=50)  
   

class Colegio(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdColegio = models.IntegerField(unique=True)  
    NombColegio = models.CharField(max_length=50)  
    IdTipo = models.ForeignKey('Tipo', on_delete=models.DO_NOTHING, db_column='IdTipo')  
    IdRegion = models.ForeignKey('Region', on_delete=models.DO_NOTHING, db_column='IdRegion')  
    IdComuna = models.ForeignKey('Comuna', on_delete=models.DO_NOTHING, db_column='IdComuna')  
    IdCiudad = models.ForeignKey('Ciudad', on_delete=models.DO_NOTHING, db_column='IdCiudad')  
    Direccion = models.TextField(blank=True, null=True)  

    

class Libro(models.Model):
    Id = models.AutoField(primary_key=True) 
    IdLibro = models.IntegerField(unique=True)  
    Nombre = models.TextField()  
    Descripcion = models.TextField(blank=True, null=True)  
    Autor = models.TextField(blank=True, null=True)  
    FechaPublicacion = models.DateField(blank=True, null=True)  
    IdUbicacion = models.ForeignKey('Ubicacion', on_delete=models.DO_NOTHING, db_column='IdUbicacion')  
    
    
class Usuario(models.Model):
    Id = models.AutoField(primary_key=True) 
    rut = models.IntegerField(unique=True) 
    dv = models.CharField(max_length=1)  
    Nombres = models.TextField() 
    ApePat = models.TextField()  
    ApeMat = models.TextField(blank=True, null=True)  
    Email = models.EmailField(blank=True, null=True)  
    Telefono = models.IntegerField(blank=True, null=True)  
    IdColegio = models.ForeignKey('Colegio', on_delete= models.DO_NOTHING, db_column='IdColegio') 
    IdRol = models.ForeignKey('Rol', on_delete=models.DO_NOTHING, db_column='IdRol')  
    IdEstado = models.ForeignKey('Usuarioestado', on_delete=models.DO_NOTHING, db_column='IdEstado')  

   
class Reserva(models.Model):
    Id = models.AutoField(primary_key=True) 
    NroReserva = models.IntegerField(unique=True) 
    Rut = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, db_column='rut') 
    IdColegio = models.ForeignKey('Colegio', on_delete=models.DO_NOTHING, db_column='IdColegio') 
    IdLibro = models.ForeignKey('Libro', on_delete=models.DO_NOTHING, db_column='IdLibro')  
    FechaPrestamo = models.DateTimeField()  
    FechaDevolucion = models.DateTimeField()  
    IdEstado = models.ForeignKey('Estado', on_delete=models.DO_NOTHING, db_column='IdEstado')  

   

class Stock(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)
    IdColegio = models.ForeignKey('Colegio', on_delete=models.DO_NOTHING, db_column='IdColegio', related_name='stocks_colegio')
    IdLibro = models.ForeignKey('Libro', on_delete=models.DO_NOTHING, db_column='IdLibro', related_name='stocks_libro')
    Nombre = models.ForeignKey('Libro', on_delete=models.DO_NOTHING, db_column='Nombre', related_name='stocks_nombre')
    Cantidad = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)



   