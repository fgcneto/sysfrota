from Usuario.models import Usuario
from Veiculo.models import RotaVeiculo, Veiculo
from django.db import models


class Agenda(models.Model):

    """
        Responsável pela Gestão dos agendamentos 
        da saída de veículos
    """

    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now=True)
    is_active = models.BooleanField(default=True)
    descricao = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='Descrição do Agendamento')
    data_saida = models.DateField(
        null=True, blank=True, verbose_name="Data da Saída")
    data_retorno = models.DateField(
        null=True, blank=True, verbose_name="Data do Retorno")
    hora_saida = models.TimeField(
        null=True, blank=True, verbose_name="Hora da Saída")
    hora_retorno = models.TimeField(
        null=True, blank=True, verbose_name="Hora do Retorno")
    rotas_veiculos = models.ManyToManyField(RotaVeiculo)
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.RESTRICT,
        related_name="veiculo_agenda",
        verbose_name="Veículo"
    )
    motorista = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="motorista_agenda",
        verbose_name="Motorista"
    )
    usuario_cadastro = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT,
        related_name="usuario_cadastro_agenda",
        verbose_name="Administrador"
    )

    def __str__(self):
        return str(self.descricao) + " - " + str(self.veiculo) + " - " + str(self.motorista) + " - " + str(self.data_saida) + " - " + str(self.hora_saida)

    class Meta:
        ordering = ['data_saida', 'hora_saida']
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
