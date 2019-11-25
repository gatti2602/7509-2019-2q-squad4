from django.urls import path

from . import views

app_name = 'proyecto'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cod_proyecto>/', views.project_detail, name='project_detail'),
    path('<int:cod_proyecto>/riesgo/crear', views.riesgo_create, name='riesgo_create'),
    path('<int:cod_proyecto>/riesgo/<int:cod_riesgo>', views.riesgo_detail, name='riesgo_detail'),

]
