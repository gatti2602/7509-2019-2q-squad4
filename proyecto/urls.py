from django.urls import path
from . import views

app_name = 'proyecto'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cod_proyecto>/', views.detail, name='detail'),
]
