from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from proyecto.forms import ProyectoForm, RiesgoForm, RiesgoCreateForm, IteracionForm
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
                                                    'risks': proyecto.riesgo_set.all(),
                                                    'iters': proyecto.iteracion_set.order_by('fecha_desde').all})


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


def riesgo_create(request, cod_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=cod_proyecto)
    if request.method == 'POST':
        riesgoForm = RiesgoCreateForm(request.POST)
        if riesgoForm.is_valid():
            proyecto.CrearRiesgo(riesgoForm.cleaned_data.get('descripcion'),
                                 riesgoForm.cleaned_data.get('probabilidad'),
                                 riesgoForm.cleaned_data.get('impacto'))
            return HttpResponseRedirect(reverse('proyecto:project_detail', args=(proyecto.cod_proyecto,)))
    else:
        riesgoForm = RiesgoCreateForm()
    return render(request, 'riesgo/detail.html', {'form': riesgoForm})


def iteracion_create(request, cod_proyecto):
    proyecto = get_object_or_404(Proyecto, pk=cod_proyecto)
    if request.method == 'POST':
        iteracionForm = IteracionForm(request.POST, cod_proyecto=cod_proyecto)
        if iteracionForm.is_valid():
            proyecto.CrearIteracion(iteracionForm.cleaned_data.get('fecha_desde'),
                                    iteracionForm.cleaned_data.get('fecha_hasta'))
            return HttpResponseRedirect(reverse('proyecto:project_detail', args=(proyecto.cod_proyecto,)))
    else:
        iteracionForm = IteracionForm(cod_proyecto=cod_proyecto)
    return render(request, 'iteracion/detail.html', {'form': iteracionForm})
