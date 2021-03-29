from django.shortcuts import render
from .models import Noticia,Proyecto

# Create your views here.
def index(request):
    noticias = Noticia.objects.all()
    proyectos = Proyecto.objects.all()
    context = {
        "noticias":noticias,
        "proyectos": proyectos,
    }
    return render(request, 'index.html', context)