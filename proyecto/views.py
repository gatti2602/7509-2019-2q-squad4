from django.shortcuts import render
from proyecto.models import Proyecto


def index(request):
    listaProyectos = Proyecto.objects.all()
    context = {
        'lista_proyectos': listaProyectos,
    }
    return render(request, 'proyecto/index.html', context)


def detail(request, cod_proyecto):
    return render(request, 'proyecto/detail.html')

