from django.forms import ModelForm
from .models import Agenda


class EditAgendamentoForm(ModelForm):

    class Meta:
        model = Agenda
        fields = ('descricao', 'data_saida', 'data_retorno', 'hora_saida',
                  'hora_retorno', 'rotas_veiculos', 'veiculo', 'motorista', 'usuario_cadastro')
