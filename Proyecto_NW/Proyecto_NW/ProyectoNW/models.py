from django.db import models

# Create your models here.
class Artista(models.Model):
    Id_Artista = models.IntegerField(db_column='Id_Artista', primary_key=True)  # Field name made lowercase.
    nom_artista = models.CharField(db_column='nom_Artista', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Id_Genero = models.ForeignKey('genero', models.DO_NOTHING, db_column='Id_Genero', to_field='Id_Genero', blank=True, null=True)  # Field name made lowercase.
    anno_nac = models.IntegerField(blank=True, null=True)
    Id_nacion = models.ForeignKey('nacionalidad', models.DO_NOTHING, db_column='Id_nacion',to_field='Id_nacion')  # Field name made lowercase.
    Id_Estilo = models.ForeignKey('estilo', models.DO_NOTHING, db_column='Id_Estilo',to_field='Id_Estilo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artista'


class Canciones(models.Model):
    Id_Cancion = models.IntegerField(db_column='Id_Cancion', primary_key=True)  # Field name made lowercase.
    Id_Artista = models.ForeignKey(Artista, models.DO_NOTHING, db_column='Id_Artista', blank=True, null=True)  # Field name made lowercase.
    Album = models.CharField(db_column='Album', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cancion = models.CharField(max_length=50, blank=True, null=True)
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    vendidas = models.IntegerField(blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canciones'


class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=52)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=13)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=26)  # Field name made lowercase.
    surfacearea = models.FloatField(db_column='SurfaceArea')  # Field name made lowercase.
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    lifeexpectancy = models.FloatField(db_column='LifeExpectancy', blank=True, null=True)  # Field name made lowercase.
    gnp = models.FloatField(db_column='GNP', blank=True, null=True)  # Field name made lowercase.
    gnpold = models.FloatField(db_column='GNPOld', blank=True, null=True)  # Field name made lowercase.
    localname = models.CharField(db_column='LocalName', max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Estilo(models.Model):
    Id_Estilo = models.IntegerField(db_column='Id_Estilo', primary_key=True)  # Field name made lowercase.
    nom_estilo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estilo'


class Genero(models.Model):
    Id_Genero = models.IntegerField(db_column='Id_Genero', primary_key=True)  # Field name made lowercase.
    nom_Genero = models.CharField(db_column='nom_Genero', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genero'


class Nacionalidad(models.Model):
    Id_nacion = models.IntegerField(db_column='Id_nacion', primary_key=True)  # Field name made lowercase.
    nom_nacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nacionalidad'
        

