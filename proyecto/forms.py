from django import forms

from proyecto.models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['cod_proyecto', 'titulo', 'descripcion', 'fecha_inicio_req', 'fecha_fin_req']
