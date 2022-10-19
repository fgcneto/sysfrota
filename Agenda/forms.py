from django.forms import ModelForm
from django.utils.translation import gettext as _
from django import forms
from .models import Agenda


class EditAgendamentoForm(ModelForm):

    class Meta:
        model = Agenda
        fields = ('descricao', 'data_saida',
                  'data_retorno', 'veiculo', 'motorista')


class AgendamentoForm(ModelForm):

    class Meta:
        model = Agenda

        fields = ('descricao', 'data_saida',
                  'data_retorno', 'veiculo', 'motorista')

        labels = {
            'descricao': _('Descrição'),
            'data_saida': _('Data da Saída'),
            'data_retorno': _('Data do Retorno'),
            'veiculo': _('Veículo'),
            'motorista': _('Motorista')
        }

        widgets = {
            'descricao': forms.TextInput(
                attrs={'id': 'descricao', 'class': 'form-control'}),
            'data_saida': forms.TextInput(
                attrs={'id': 'data_saida', 'class': 'form-control'}),
            'data_retorno': forms.TextInput(
                attrs={'id': 'data_retorno', 'class': 'form-control'}),
            'veiculo': forms.Select(
                attrs={'id': 'veiculo',
                       'class': 'form-control'}),
            'motorista': forms.Select(
                attrs={'id': 'motorista',
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}
