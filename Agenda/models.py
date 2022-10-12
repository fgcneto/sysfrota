from Usuario.models import Usuario
from Veiculo.models import Veiculo
from django.db import models


class Agenda(models.Model):

    """
        Responsável pela Gestão dos agendamentos 
        da saída de veículos
    """

    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now_add=True)
    descricao = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='Descrição do Agendamento')
    data_saida = models.DateTimeField(
        verbose_name="Data e Hora da Saída")
    data_retorno = models.DateTimeField(
        verbose_name="Data do Retorno")
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT,
        related_name="veiculo_agenda",
        verbose_name="Veículo"
    )
    motorista = models.ForeignKey(
        Usuario, on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="motorista_agenda",
        verbose_name="Motorista"
    )
    usuario_cadastro = models.ForeignKey(
        Usuario, on_delete=models.PROTECT,
        related_name="usuario_cadastro_agenda",
        verbose_name="Usuário do cadastro"
    )

    def __str__(self):
        return str(self.veiculo) + " - " + str(self.data_saida)

    class Meta:
        ordering = ['-data_saida']
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
