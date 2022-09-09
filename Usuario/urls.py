from django.urls import path

from django.contrib.auth import views as auth_views
from Usuario import views


app_name = 'usuario'

urlpatterns = [
    path('listar-usuarios', views.UsuarioListView.as_view(),
         name='listar_usuarios'),
    path('editar-usuario/<int:pk>',
         views.UsuarioEditView.as_view(), name='editar_usuario'),
    path('deletar-usuario/<int:pk>',
         views.UsuarioDeleteView.as_view(), name='deletar_usuario'),
]
