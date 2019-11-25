from django.contrib import admin

# Register your models here.
from proyecto.models import Proyecto, RiesgoImpacto, Riesgo

admin.site.register(Proyecto)
admin.site.register(Riesgo)
admin.site.register(RiesgoImpacto)
