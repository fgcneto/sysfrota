from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext as _
from .models import Veiculo


class EditVeiculoForm(ModelForm):

    class Meta:
        model = Veiculo
        fields = ('marca', 'tipo', 'placa',
                  'kilometragem', 'ano_fabricacao')


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = (
            'marca', 'tipo', 'placa',
            'kilometragem', 'ano_fabricacao'
        )

        labels = {
            'marca': _('Marca'),
            'tipo': _('Modelo'),
            'placa': _('Placa'),
            'kilometragem': _('Kilometragem'),
            'ano_fabricacao': _('Ano de Fabricacao'),
        }

        widgets = {
            'marca': forms.TextInput(
                attrs={'id': 'color', 'class': 'form-control'}),
            'tipo': forms.TextInput(
                attrs={'id': 'tipo', 'autofocus': True,
                       'class': 'form-control'}),
            'placa': forms.TextInput(
                attrs={'id': 'placa', 'autofocus': True,
                       'class': 'form-control'}),
            'kilometragem': forms.NumberInput(
                attrs={'id': 'kilometragem', 'autofocus': True,
                       'class': 'form-control'}),
            'ano_fabricacao': forms.DateInput(
                attrs={'id': 'ano_fabricacao', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}
