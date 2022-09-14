from django.forms import ModelForm
from .models import LiberarVeiculo


class EditLiberarVeiculoForm(ModelForm):

    class Meta:
        model = LiberarVeiculo
        fields = ('observacoes', 'agendamento', 'responsavel_liberacao', 'porteiro_saida',
                  'porteiro_chegada', 'confirmacao_saida', 'confirmacao_chegada', 'km_saida', 'km_chegada', 'data_hora_saida', 'data_hora_chegada')
