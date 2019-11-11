from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Feature


def index_feature(request):
    feature_list = Feature.objects.all()
    context = {
        'features_list': feature_list,
    }
    return render(request, 'producto/index_feature.html', context)


def post_feature(request):
    if len(request.POST) == 0:
        return render(request, 'producto/post_feature.html', {})

    try:
        new_feature = Feature()
        new_feature.description = request.POST['description']
        new_feature.status = request.POST['status']
        new_feature.expected_delivery = datetime.strptime(request.POST['expected_date'], '%Y-%m-%d')
    except Exception as e:
        # Redisplay the question voting form.
        return render(request, 'producto/post_feature.html', {
            'error_message': e,
        })
    else:
        new_feature.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('producto:index_feature', args=()))
