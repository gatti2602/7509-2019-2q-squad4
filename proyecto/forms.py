from django import forms

from proyecto.models import Proyecto, Riesgo, Iteracion


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
        probabilidad = cleaned_data.get('probabilidad')

        if probabilidad > 1.0 or probabilidad < 0.0:
            raise forms.ValidationError("Probabilidad debe estar entre 0.0 y 1.0")

        if fecha_cierre is None:
            return

        if fecha_cierre < fecha_alta:
            raise forms.ValidationError("Fecha Cierre no puede ser anterior a fecha de alta")

    class Meta:
        model = Riesgo
        fields = ['descripcion', 'fecha_cierre', 'probabilidad', 'presentado', 'impacto']


class RiesgoCreateForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        probabilidad = cleaned_data.get('probabilidad')

        if probabilidad > 1.0 or probabilidad < 0.0:
            raise forms.ValidationError("Probabilidad debe estar entre 0.0 y 1.0")

    class Meta:
        model = Riesgo
        fields = ['descripcion', 'probabilidad', 'impacto']


class IteracionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.cod_proyecto = kwargs.pop('cod_proyecto')
        super(IteracionForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        fecha_desde = cleaned_data.get('fecha_desde')
        fecha_hasta = cleaned_data.get('fecha_hasta')

        if fecha_desde >= fecha_hasta:
            raise forms.ValidationError('Fecha Desde debe ser anterior a Fecha Hasta')

        # TODO: Agregar validaciones de solapamiento
        it = Iteracion.objects.filter(proyecto__cod_proyecto=self.cod_proyecto,
                                      fecha_desde__lte=fecha_hasta,
                                      fecha_hasta__gte=fecha_desde)

        if it.count() > 0:
            raise forms.ValidationError('Iteraciones se solapan')

    class Meta:
        model = Iteracion
        fields = ['fecha_desde', 'fecha_hasta']
