from django.urls import path
from Veiculo import views

app_name = "veiculo"

urlpatterns = [
    path('cadastrar-veiculo',
         views.veiculo_create,
         name='cadastrar_veiculo'),
    path("listar-veiculos/", views.VeiculoListView.as_view(),
         name="listar_veiculos"),
    path('editar-veiculo/<int:pk>',
         views.veiculo_edit, name='editar_veiculo'),
    path('deletar-veiculo/<int:pk>',
         views.veiculo_delete, name='deletar_veiculo'),
]
