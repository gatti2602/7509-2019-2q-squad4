from datetime import datetime

from django.db import models


class Proyecto(models.Model):
    """
    Clase principal para guardar los proyectos de la compañia
    """

    #Fields
    cod_proyecto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)
    fecha_inicio_real = models.DateField()
    fecha_fin_real = models.DateField()

    #Audit
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_modif = models.DateField(auto_now=True)

    def CrearRiesgo(self, desc, prob, imp):
        riesgo = Riesgo(descripcion=desc, probabilidad=prob, impacto=imp)
        riesgo.proyecto = self
        riesgo.save()

    def ObtenerExposicion(self):
        exposicion = 0
        riesgos = self.riesgo_set.exclude(fecha_cierre__lte=datetime.now())
        for riesgo in riesgos:
            exposicion = exposicion + riesgo.probabilidad * riesgo.impacto.impacto
        if riesgos.count() > 0:
            exposicion = exposicion / riesgos.count()
        return round(exposicion, 2)


class RiesgoImpacto(models.Model):
    """
    Impacto de los riesgos de presentarse
    """

    # fields
    descripcion = models.TextField(max_length=50)
    impacto = models.FloatField()

    def __str__(self):
        return self.descripcion


class Riesgo(models.Model):
    """
    Riesgos asociados a los proyectos
    """

    # Fields
    descripcion = models.CharField(max_length=50)
    fecha_cierre = models.DateField(null=True)
    probabilidad = models.FloatField()
    presentado = models.BooleanField(default=False)

    # Audit
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_modif = models.DateField(auto_now=True)

    # Foreigns
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    impacto = models.ForeignKey(RiesgoImpacto, on_delete=models.PROTECT)
