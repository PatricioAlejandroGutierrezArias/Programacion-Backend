from django.shortcuts import render
from .models import Artista


# Create your views here.
def index(request):
    return render(request, 'index.html')

def artistas(request):
    artistas = Artista.objects.all()
    data = {'artistas': artistas}
    return render(request, 'artistas.html',data)