from django.contrib.auth import forms
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from .models import Usuario


import sweetify
from sweetify.views import SweetifySuccessMixin


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('user_type', 'first_name', 'last_name', 'username',
                  'password', 'email', 'cpf', 'matricula', 'habilitacao')
        labels = {
            'user_type': _('Tipo de Usuário'),
            'first_name': _('Primeiro Nome'),
            'last_name': _('Último Nome'),
            'username': _('Usuário do sistema'),
            'password': _('Senha'),
            'email': _('E-mail'),
            'cpf': _('CPF'),
            'matricula': _('Matrícula'),
            'habilitacao': _('Habilitação'),
        }
        widgets = {
            'user_type': forms.Select(
                attrs={'id': 'user_type', 'class': 'form-control'}),
            'first_name': forms.TextInput(
                attrs={'id': 'first_name', 'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'id': 'last_name', 'class': 'form-control'}),
            'username': forms.TextInput(
                attrs={'id': 'username', 'class': 'form-control'}),
            'password': forms.PasswordInput(
                attrs={'id': 'password', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control'}),
            'cpf': forms.TextInput(
                attrs={'id': 'cpf', 'class': 'form-control'}),
            'matricula': forms.TextInput(
                attrs={'id': 'matricula', 'class': 'form-control'}),
            'habilitacao': forms.TextInput(
                attrs={'id': 'habilitacao', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = "__all__"

# class EditUsuarioForm(forms.UserChangeForm):
#     class Meta(forms.UserChangeForm.Meta):
#         model = Usuario
#         fields = ('user_type', 'first_name', 'last_name', 'username',
#                   'password', 'email', 'cpf', 'matricula', 'habilitacao')


# class UsuarioForm(ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ('user_type', 'first_name', 'last_name', 'username',
#                   'password', 'email', 'cpf', 'matricula', 'habilitacao'
#                   )

#         labels = {
#             'user_type': _('Função'),
#             'first_name': _('Nome'),
#             'last_name': _('Sobrenome'),
#             'username': _('Nome de usuário'),
#             'password': _('Senha'),
#             'email': _('E-mail'),
#             'cpf': _('CPF'),
#             'matricula': _('Matrícula'),
#             'habilitacao': _('Habilitação'),
#         }

#         widgets = {
#             'user_type': forms.Select(
#                 attrs={'id': 'color', 'class': 'form-control'}),
#             'first_name': forms.TextInput(
#                 attrs={'id': 'first_name', 'autofocus': True,
#                        'class': 'form-control'}),
#             'last_name': forms.TextInput(
#                 attrs={'id': 'last_name', 'autofocus': True,
#                        'class': 'form-control'}),
#             'username': forms.TextInput(
#                 attrs={'id': 'username', 'autofocus': True,
#                        'class': 'form-control'}),
#             'password': forms.PasswordInput(
#                 attrs={'id': 'password', 'autofocus': True,
#                        'class': 'form-control'}),
#             'email': forms.EmailInput(
#                 attrs={'id': 'email', 'autofocus': True,
#                        'class': 'form-control'}),
#             'cpf': forms.TextInput(
#                 attrs={'id': 'cpf',
#                        'class': 'form-control',
#                        'placeholder': '___.___.___-__',
#                        'onkeyup': "mascara('###.###.###-##',this,event,false)"
#                        }),
#             'matricula': forms.TextInput(
#                 attrs={'id': 'matricula', 'autofocus': True,
#                        'class': 'form-control'}),
#             'habilitacao': forms.TextInput(
#                 attrs={'id': 'habilitacao', 'autofocus': True,
#                        'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(UsuarioForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.error_messages = \
#                 {'required': 'O(A) {fieldname} é obrigatório.'.
#                     format(fieldname=field.label)}
