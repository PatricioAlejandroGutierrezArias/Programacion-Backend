"""
URL configuration for Gutierrez_Patricio_Final project.

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
from Gutierrez_P_Finalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registroparticipantes/',views.registroparticipantes,name='registroparticipantes'),
    path('registroinstituciones/',views.registroinstituciones,name='registroinstituciones'),
    path('participantes/', views.participantes_list.as_view(), name='participantes-list'),
    path('participantes/<int:id>/', views.participantes_detail.as_view()),
    path('instituciones/', views.instituciones_list),
    path('instituciones/<int:id>/', views.instituciones_detail),
    path('api/autorproyecto/', views.AutorProyectoDetail.as_view())
]
