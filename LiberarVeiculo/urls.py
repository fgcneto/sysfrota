from django.urls import path

from LiberarVeiculo import views

app_name = "liberarveiculo"

urlpatterns = [
    path('cadastrar-liberar-veiculo/', views.CadastrarLiberarVeiculo.as_view(),
         name="cadastrar_liberar_veiculo"),
    path("listar-liberar-veiculos/", views.LiberarVeiculoListView.as_view(),
         name="listar_liberar_veiculos"),
    path('editar-liberar-veiculo/<int:pk>',
         views.LiberarVeiculoEditView.as_view(), name='editar_liberar_veiculo'),
    path('deletar-liberar-veiculo/<int:pk>',
         views.liberar_veiculo_delete, name='deletar_liberar_veiculo')
]
