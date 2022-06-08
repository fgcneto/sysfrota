from django.urls import path

from django.contrib.auth import views as auth_views
from Usuario import views


app_name = 'usuario'

urlpatterns = [
    path('listar_administrativo', views.ListarAdministrativo.as_view(),
         name='listar_administrativo')
]
