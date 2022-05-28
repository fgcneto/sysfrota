from django.db import models


class Veiculo(models.Model):
    marca = models.CharField(
        max_length=20, verbose_name='Marca')
    tipo = models.CharField(
        max_length=20, verbose_name='Tipo')
    placa = models.CharField(
        max_length=10, unique=True, verbose_name='Placa')
    kilometragem = models.PositiveIntegerField(
        verbose_name='Kilometragem')
    ano_fabricacao = models.PositiveIntegerField(
        verbose_name="Ano de Fabricação")

    def __str__(self):
        return self.tipo + " " + self.placa

    class Meta:
        ordering = ['marca', 'tipo']
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
