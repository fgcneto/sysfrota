from django.urls import path

from Veiculo import views

app_name = "veiculo"

urlpatterns = [
    path('cadastrar-veiculo/', views.CadastrarVeiculo.as_view(),
         name="cadastrar_veiculo"),
    path("listar-veiculos/", views.VeiculoListView.as_view(),
         name="listar_veiculos"),
    path('editar-veiculo/<int:pk>',
         views.VeiculoEditView.as_view(), name='editar_veiculo'),
    path('deletar-veiculo/<int:pk>',
         views.veiculo_delete, name='deletar_veiculo'),
]
