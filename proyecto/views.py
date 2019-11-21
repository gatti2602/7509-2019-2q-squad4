from django.shortcuts import render, get_object_or_404

from proyecto.forms import ProyectoForm
from proyecto.models import Proyecto


def index(request):
    listaProyectos = Proyecto.objects.all()
    context = {
        'lista_proyectos': listaProyectos,
    }
    return render(request, 'proyecto/index.html', context)


def detail(request, cod_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=cod_proyecto)
    form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto/detail.html', {'form': form})

