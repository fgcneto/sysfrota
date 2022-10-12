from django.db import models
from Agenda.models import Agenda
from Usuario.models import Usuario


class LiberarVeiculo(models.Model):
    """
      Responsável pela Gestão da liberação de Veiculos
    """
    observacoes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Observações")
    agendamento = models.ForeignKey(
        Agenda, on_delete=models.RESTRICT,
        related_name="agendamento_liberacao_veiculo",
        verbose_name="Agenda")
    responsavel_liberacao = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT,
        related_name="responsavel_liberacao_veiculo",
        verbose_name="Pesponsável pela liberação")
    porteiro_saida = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT,
        null=True, blank=True,
        related_name="porteiro_saida_liberacao_veiculo",
        verbose_name="Porteiro da Saída")
    porteiro_chegada = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT,
        null=True, blank=True,
        related_name="porteiro_chegada_liberacao_veiculo",
        verbose_name="Porteiro da chegada")
    confirmacao_saida = models.BooleanField(
        null=True,
        verbose_name="Assinatura do Porteiro na Saída")
    confirmacao_chegada = models.BooleanField(
        null=True,
        verbose_name="Assinatura do Porteiro na Chegada")
    km_saida = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Kilometragem de Saída")
    km_chegada = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Kilometragem de Chegada")
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now_add=True)
    data_hora_saida = models.DateTimeField(
        null=True, blank=True, verbose_name="Data e Hora da Saída")
    data_hora_chegada = models.DateTimeField(
        null=True, blank=True, verbose_name="Data e Hora da Chegada")

    def __str__(self):
        return str(self.agendamento) + " - " + str(self.responsavel_liberacao) + " - " + str(self.agendamento.motorista) + " - " + str(self.agendamento.veiculo) + " - " + str(self.agendamento.hora_saida)

    class Meta:
        ordering = ['-agendamento']
        verbose_name = "Liberar Veículo"
        verbose_name_plural = "Liberar Veículos"
