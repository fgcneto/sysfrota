from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('user_type', 'first_name', 'last_name', 'username',
                  'email', 'cpf', 'matricula', 'habilitacao', 'password1', 'password2')
        labels = {
            'user_type': _('Tipo de Usuário'),
            'first_name': _('Primeiro Nome'),
            'last_name': _('Último Nome'),
            'username': _('Usuário do sistema'),
            'password1': _('Senha do Usuário'),
            'password2': _('Confirmação da Senha'),
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
            'password1': forms.TextInput(
                attrs={'id': 'password1', 'class': 'form-control'}),
            'password2': forms.TextInput(
                attrs={'id': 'password2', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control'}),
            'cpf': forms.TextInput(
                attrs={'id': 'cpf', 'class': 'form-control'}),
            'matricula': forms.TextInput(
                attrs={'id': 'matricula', 'class': 'form-control'}),
            'habilitacao': forms.TextInput(
                attrs={'id': 'habilitacao', 'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('user_type', 'first_name', 'last_name', 'username',
                  'password', 'email', 'cpf', 'matricula', 'habilitacao')
        labels = {
            'user_type': _('Tipo de Usuário'),
            'first_name': _('Primeiro Nome'),
            'last_name': _('Último Nome'),
            'username': _('Usuário'),
            'password': _('Password'),
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
            'password': forms.TextInput(
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

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
