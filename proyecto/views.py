from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from proyecto.forms import ProyectoForm, RiesgoForm
from proyecto.models import Proyecto


def index(request):
    listaProyectos = Proyecto.objects.all()
    context = {
        'lista_proyectos': listaProyectos,
    }
    return render(request, 'proyecto/index.html', context)


def project_detail(request, cod_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=cod_proyecto)
    form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto/detail.html', {'form': form,
                                                    'proyecto': proyecto,
                                                    'risks': proyecto.riesgo_set.all()})


def riesgo_detail(request, cod_proyecto, cod_riesgo):
    proyecto = get_object_or_404(Proyecto, pk=cod_proyecto)
    riesgo = proyecto.riesgo_set.get(pk=cod_riesgo)
    if request.method == 'POST':
        riesgoForm = RiesgoForm(request.POST, instance=riesgo)
        if riesgoForm.is_valid():
            riesgoForm.save()
            return HttpResponseRedirect(reverse('proyecto:project_detail', args=(proyecto.cod_proyecto,)))
    else:
        riesgoForm = RiesgoForm(instance=riesgo)
    return render(request, 'riesgo/detail.html', {'form': riesgoForm})
