from django.urls import path
from django.contrib.auth import views as auth_views
from Agenda import views


app_name = 'agenda'

urlpatterns = [
    path('cadastrar-agendamento',
         views.AgendaRegisterView.as_view(), name='cadastrar_agendamento'),
]
