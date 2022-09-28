
from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField


class Usuario(AbstractUser):
    """
        Responsável pela Gestão do Usuários do Sistema
    """
    USER_TYPE_CHOICES = (
        (1, 'Administrativo'),
        (2, 'Motorista'),
        (3, 'Porteiro'),
    )
    user_type = models.PositiveSmallIntegerField(
        verbose_name='Tipo de Usuário', choices=USER_TYPE_CHOICES)
    cpf = CPFField('cpf', unique=True, null=True, blank=True)
    habilitacao = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Habilitação')
    matricula = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Matrícula')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
