from django.forms import ModelForm
from django import forms
from .models import Agenda


class EditAgendamentoForm(ModelForm):

    class Meta:
        model = Agenda
        fields = ('descricao', 'data_saida', 'data_retorno', 'hora_saida',
                  'hora_retorno', 'veiculo', 'motorista', 'usuario_cadastro')
