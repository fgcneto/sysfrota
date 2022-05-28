from django.contrib.auth import forms

from .models import Usuario, Administrador, Porteiro, Motorista


class AlterarUsuarioForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario


class SalvarUsuarioForm():
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario


class AlterarAdministradorForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Administrador


class SalvarAdministradorForm():
    class Meta(forms.UserChangeForm.Meta):
        model = Administrador


class AlterarPorteiroForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Porteiro


class SalvarPorteiroForm():
    class Meta(forms.UserChangeForm.Meta):
        model = Porteiro


class AlterarMotoristaForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Motorista


class SalvarMotoristaForm():
    class Meta(forms.UserChangeForm.Meta):
        model = Motorista
