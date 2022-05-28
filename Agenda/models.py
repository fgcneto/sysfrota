from Usuario.models import Administrador, Motorista
from Veiculo.models import Veiculo
from django.db import models


class Agenda(models.Model):
    """
        Responsável pela Gestão dos agendamentos 
        da saída de veículos
    """
    destino = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Destino')
    descricao = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Descrição')
    data_saida = models.DateField(
        null=True, blank=True, verbose_name="Data da Saída")
    data_retorno = models.DateField(
        null=True, blank=True, verbose_name="Data do Retorno")
    hora_saida = models.TimeField(
        null=True, blank=True, verbose_name="Hora da Saída")
    hora_retorno = models.TimeField(
        null=True, blank=True, verbose_name="Hora do Retorno")
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.RESTRICT, related_name="veiculo", verbose_name="Veículo")
    motorista = models.ForeignKey(
        Motorista, on_delete=models.RESTRICT, related_name="motorista", verbose_name="Motorista")
    usuario_cadastro = models.ForeignKey(
        Administrador, on_delete=models.RESTRICT, related_name="administrador", verbose_name="Administrador")

    def __str__(self):
        return str(self.descricao) + " - " + str(self.veiculo) + " - " + str(self.motorista) + " - " + str(self.data_saida) + " - " + str(self.hora_saida)

    class Meta:
        ordering = ['data_saida', 'hora_saida']
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
