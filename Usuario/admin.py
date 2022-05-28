from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from Usuario.models import Administrador, Usuario, Motorista, Porteiro
from .forms import \
    AlterarAdministradorForm, AlterarUsuarioForm, SalvarAdministradorForm, SalvarUsuarioForm, \
    AlterarAdministradorForm, SalvarAdministradorForm, \
    AlterarMotoristaForm, SalvarMotoristaForm, \
    AlterarPorteiroForm, SalvarPorteiroForm

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Porteiro)
admin.site.register(Motorista)


# @admin.register(Usuario)
# class UserAdmin(auth_admin.UserAdmin):
#     form = AlterarUsuarioForm
#     add_form = SalvarUsuarioForm
#     model = Usuario
#     fieldsets = auth_admin.UserAdmin.fieldsets + (
#         ("Campos Adicionais", {"fields": ("cpf",)}),
#     )


# @admin.register(Administrador)
# class UserAdmin(auth_admin.UserAdmin):
#     form = AlterarAdministradorForm
#     add_form = SalvarAdministradorForm
#     model = Usuario
#     fieldsets = auth_admin.UserAdmin.fieldsets + (
#         ("Campos Adicionais", {"fields": ("matricula", "funcao")}),
#     )


# @admin.register(Motorista)
# class UserAdmin(auth_admin.UserAdmin):
#     form = AlterarMotoristaForm
#     add_form = SalvarMotoristaForm
#     model = Usuario
#     fieldsets = auth_admin.UserAdmin.fieldsets + (
#         ("Campos Adicionais", {"fields": ("habilitacao",)}),
#     )


# @admin.register(Porteiro)
# class UserAdmin(auth_admin.UserAdmin):
#     form = AlterarPorteiroForm
#     add_form = SalvarPorteiroForm
#     model = Usuario
#     fieldsets = auth_admin.UserAdmin.fieldsets + (
#         ("Campos Adicionais", {"fields": ("habilitacao",)}),
#     )
