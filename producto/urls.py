from django.urls import path
from . import views

app_name = 'producto'
urlpatterns = [
    path('feature/', views.index_feature, name='index_feature'),
    path('feature/new/', views.post_feature, name='post_feature'),
]
