from django.forms import ModelForm
from .models import Veiculo


class EditVeiculoForm(ModelForm):

    class Meta:
        model = Veiculo
        fields = ('marca', 'tipo', 'placa',
                  'kilometragem', 'ano_fabricacao')
