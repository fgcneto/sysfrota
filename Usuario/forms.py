from django.contrib.auth import forms
from django.forms import ModelForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Usuario


class EditUsuarioForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario
        fields = ('user_type', 'first_name', 'last_name', 'username',
                  'password', 'email', 'cpf', 'matricula', 'habilitacao', 'funcao')

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
