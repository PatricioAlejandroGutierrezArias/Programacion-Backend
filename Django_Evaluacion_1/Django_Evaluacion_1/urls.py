"""
URL configuration for Django_Evaluacion_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_appev import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('viento/', views.Viento, name='viento'),
    path('cuerda/', views.Cuerda, name='cuerda'),
    path('percusion/', views.Percusion, name='percusion'),
    path('usuario/', views.Usuario, name='usuario'),
    path('descripcion/<str:categoria>/<str:producto>', views.Descripcion, name='descripcion'),
    path('descripcion/<str:categoria>/<str:producto>', views.Descripcion, name='descripcion'),
    path('descripcion/<str:categoria>/<str:producto>', views.Descripcion, name='descripcion')
]
