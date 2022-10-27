from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import LiberarVeiculo


class LiberarVeiculoForm(ModelForm):

    class Meta:

        model = LiberarVeiculo

        fields = ('observacoes', 'agendamento',
                  'porteiro_saida', 'porteiro_chegada'
                  )
        labels = {
            'observacoes': _('Observações'),
            'agendamento': _('Agendamento'),
            'porteiro_saida': _('Porteiro da Saída'),
            'porteiro_chegada': _('Porteiro da Chegada')
        }

        widgets = {
            'observacoes': forms.Textarea(
                attrs={'id': 'observacoes', 'class': 'form-control'}),
            'agendamento': forms.Select(
                attrs={'id': 'agendamento',
                       'class': 'form-control'}),
            'porteiro_saida': forms.Select(
                attrs={'id': 'porteiro_saida',
                       'class': 'form-control'}),
            'porteiro_chegada': forms.Select(
                attrs={'id': 'porteiro_chegada',
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(LiberarVeiculoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class LiberarVeiculoPorteiroForm(ModelForm):

    class Meta:
        model = LiberarVeiculo
        fields = ('id', 'observacoes', 'km_saida', 'km_chegada'
                  )

        labels = {
            'observacoes': _('Observações'),
            'km_saida': _('Km Saída'),
            'km_chegada': _('Km Chegada'),
        }

        widgets = {
            'observacoes': forms.Textarea(
                attrs={'id': 'observacoes', 'class': 'form-control'}),
            'km_saida': forms.TextInput(
                attrs={'id': 'km_saida', 'class': 'form-control'}),
            'km_chegada': forms.TextInput(
                attrs={'id': 'km_chegada', 'autofocus': True,
                       'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(LiberarVeiculoPorteiroForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}
