from django.db import models

# Create your models here.

class EstadoProyecto(models.Model):
    '''
    Se crean los estados como clase aparte.
    Esto permitirá definir las transiciones posibles de estados en el futuro y
    detallar mas estados sin modficar el codigo
    '''
    cod_estado = models.CharField(max_length=2, primary_key=True)
    descripcion = models.CharField(max_length=50)

class Proyecto(models.Model):
    '''
    Clase principal para guardar los proyectos de la compañia
    '''

    #Fields
    cod_proyecto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)
    fecha_inicio_req = models.DateField()
    fecha_fin_req = models.DateField()

    #Audit
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modif = models.DateField(auto_now=True)

    #Foreigns
    estado_proyecto = models.ForeignKey(EstadoProyecto, on_delete=models.PROTECT)



