from pyexpat import model
from django.db import models

from Agenda.models import Agenda
from Usuario.models import Administrador, Porteiro


class LiberarVeiculo(models.Model):
    """
      Responsável pela Gestão da liberação de Veiculos
    """

    observacoes = models.TextField(
        null=True, blank=True, verbose_name="Observações")
    agendamento = models.ForeignKey(
        Agenda, on_delete=models.RESTRICT, related_name="agenda", verbose_name="Agenda")
    responsavel_liberacao = models.ForeignKey(
        Administrador, on_delete=models.RESTRICT, related_name="administrador", verbose_name="Administrador")
    porteiro_saida = models.ForeignKey(
        Porteiro, on_delete=models.RESTRICT, related_name="porteiro_saida", verbose_name="Porteiro")
    porteiro_chegada = models.ForeignKey(
        Porteiro, on_delete=models.RESTRICT, related_name="porteiro_chegada", verbose_name="Porteiro")
    assinatura_motorista_saida = models.BooleanField(
        verbose_name="Assinatura do Porteiro na Saída")
    assinatura_motorista_chegada = models.BooleanField(
        verbose_name="Assinatura do Porteiro na Chegada")
    km_saida = models.IntegerField(
        verbose_name="Kilometragem de Saída")
    km_chegada = models.ImageField(
        verbose_name="Kilometragem de Chegada")
