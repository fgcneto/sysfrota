
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
        Agenda, on_delete=models.RESTRICT, related_name="agenda_veiculo", verbose_name="Agenda")
    responsavel_liberacao = models.ForeignKey(
        Administrador, on_delete=models.RESTRICT, related_name="administrador_veiculo", verbose_name="Administrador")
    porteiro_saida = models.ForeignKey(
        Porteiro, null=True, blank=True, on_delete=models.RESTRICT, related_name="porteiro_saida", verbose_name="Porteiro")
    porteiro_chegada = models.ForeignKey(
        Porteiro, null=True, blank=True, on_delete=models.RESTRICT, related_name="porteiro_chegada", verbose_name="Porteiro")
    assinatura_motorista_saida = models.BooleanField(
        verbose_name="Assinatura do Porteiro na Saída")
    assinatura_motorista_chegada = models.BooleanField(
        verbose_name="Assinatura do Porteiro na Chegada")
    km_saida = models.PositiveIntegerField(
        null=True, blank=True,
        verbose_name="Kilometragem de Saída")
    km_chegada = models.PositiveIntegerField(
        null=True, blank=True,
        verbose_name="Kilometragem de Chegada")

    def __str__(self):
        return str(self.agendamento) + " - " + str(self.responsavel_liberacao) + " - " + str(self.agendamento.motorista) + " - " + str(self.agendamento.veiculo) + " - " + str(self.agendamento.hora_saida)

    class Meta:
        ordering = ['agendamento', 'responsavel_liberacao']
        verbose_name = "Liberar Veículo"
        verbose_name_plural = "Liberar Veículos"
