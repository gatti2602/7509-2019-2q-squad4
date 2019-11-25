from django import forms

from proyecto.models import Proyecto, Riesgo


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['cod_proyecto', 'titulo', 'descripcion', 'fecha_inicio_real', 'fecha_fin_real']


class RiesgoForm(forms.ModelForm):
    fecha_cierre = forms.DateField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        fecha_alta = self.instance.fecha_alta
        fecha_cierre = cleaned_data.get('fecha_cierre')
        if fecha_cierre is None:
            return

        if fecha_cierre < fecha_alta:
            raise forms.ValidationError("Fecha Cierre no puede ser anterior a fecha de alta")

    class Meta:
        model = Riesgo
        fields = ['descripcion', 'fecha_cierre', 'probabilidad', 'presentado', 'impacto']
