from django.db import models

# Create your models here.


class Feature(models.Model):
    description = models.CharField(max_length=200)
    expected_delivery = models.DateTimeField('date published')
    status = models.CharField(max_length=20)
