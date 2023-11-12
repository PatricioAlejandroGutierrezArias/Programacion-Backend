from django.contrib import admin
from .models import Artista
from .models import Canciones
from .models import Genero
from .models import Country
from .models import Estilo
from .models import Nacionalidad


# Register your models here.
admin.site.register(Artista)
admin.site.register(Canciones)
admin.site.register(Genero)
admin.site.register(Estilo)
admin.site.register(Nacionalidad)