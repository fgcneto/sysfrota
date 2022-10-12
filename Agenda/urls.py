from django.urls import path
from django.contrib.auth import views as auth_views
from Agenda import views


app_name = 'agenda'

urlpatterns = [
    path('cadastrar-agendamento',
         views.AgendaRegisterView.as_view(),
         name='cadastrar_agendamento'
         ),
    path('listar-agendamentos',
         views.AgendaListView.as_view(),
         name='listar_agendamentos'
         ),
    path('porteiro-listar-agendamentos',
         views.PorteiroAgendaListView.as_view(),
         name='porteiro_listar_agendamentos'
         ),
    path('editar-agendamento/<int:pk>',
         views.AgendaEditView.as_view(),
         name='editar_agendamento'
         ),
    path('deletar-agendamento/<int:pk>',
         views.agendamento_delete,
         name='deletar_agendamento'
         ),
]
