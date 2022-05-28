
from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField


class Usuario(AbstractUser):
    cpf = CPFField('cpf', unique=True, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Motorista(Usuario):
    habilitacao = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Habilitação')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Motorista"
        verbose_name_plural = "Motoristas"


class Administrador(Usuario):
    matricula = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Matrícula')
    funcao = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Função')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Porteiro(Usuario):

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
