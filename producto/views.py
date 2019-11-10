from django.http import HttpResponse
from .models import Feature


def feature_list(request):
    feature_list = Feature.objects.all()
    output = ', '.join([f.description for f in feature_list])
    return HttpResponse(output)
