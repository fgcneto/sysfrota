from django.contrib.auth import forms
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext as _
from .models import Usuario


# class EditUsuarioForm(forms.UserChangeForm):
#     class Meta(forms.UserChangeForm.Meta):
#         model = Usuario
#         fields = ('is_active', 'user_type', 'first_name', 'last_name', 'username',
#                   'password', 'email', 'cpf', 'matricula', 'habilitacao')


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('id', 'user_type', 'first_name', 'last_name', 'username',
                  'password', 'email', 'cpf', 'matricula', 'habilitacao'
                  )

        labels = {
            'user_type': _('Função'),
            'first_name': _('Nome'),
            'last_name': _('Sobrenome'),
            'username': _('Nome de usuário'),
            'password': _('Senha'),
            'email': _('E-mail'),
            'cpf': _('CPF'),
            'matricula': _('Matrícula'),
            'habilitacao': _('Habilitação'),
        }

        widgets = {
            'user_type': forms.Select(
                attrs={'id': 'color', 'class': 'form-control'}),
            'first_name': forms.TextInput(
                attrs={'id': 'first_name', 'autofocus': True,
                       'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'id': 'last_name', 'autofocus': True,
                       'class': 'form-control'}),
            'username': forms.TextInput(
                attrs={'id': 'username', 'autofocus': True,
                       'class': 'form-control'}),
            'password': forms.PasswordInput(
                attrs={'id': 'password', 'autofocus': True,
                       'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'id': 'email', 'autofocus': True,
                       'class': 'form-control'}),
            'cpf': forms.TextInput(
                attrs={'id': 'cpf',
                       'class': 'form-control',
                       'placeholder': '___.___.___-__',
                       'onkeyup': "mascara('###.###.###-##',this,event,false)"
                       }),
            'matricula': forms.TextInput(
                attrs={'id': 'matricula', 'autofocus': True,
                       'class': 'form-control'}),
            'habilitacao': forms.TextInput(
                attrs={'id': 'habilitacao', 'autofocus': True,
                       'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = \
                {'required': 'O(A) {fieldname} é obrigatório.'.
                    format(fieldname=field.label)}

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     try:
    #         usuario_email = Usuario.objects.get(email=email)
    #     except Usuario.DoesNotExist:
    #         usuario_email = None

    #     if email == "":
    #         raise ValidationError("E-mail é um campo obrigatório.")
    #     elif usuario_email == email:
    #         raise ValidationError("Já existe uma conta com esse e-mail.")
    #     elif not validate_email(email):
    #         raise ValidationError("Esse e-mail não está válido.")

    #     return email
