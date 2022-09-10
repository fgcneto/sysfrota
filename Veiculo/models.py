from django.db import models


class Veiculo(models.Model):
    """
        Responsável pela Gestão de Veículos
    """
    marca = models.CharField(
        max_length=20,
        verbose_name='Marca')
    tipo = models.CharField(
        max_length=20,
        verbose_name='Modelo')
    placa = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa')
    kilometragem = models.PositiveIntegerField(
        verbose_name='Kilometragem')
    ano_fabricacao = models.PositiveIntegerField(
        verbose_name='Ano de Fabricação')
    created_at = models.DateTimeField(
        verbose_name='Criado em:', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Modificado em:', auto_now_add=True)

    def __str__(self):
        return self.tipo + " " + self.placa

    class Meta:
        ordering = ['marca', 'tipo']
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"


# class RotaVeiculo(models.Model):

#     """
#         Rotas dos Veículos
#     """

#     origem = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         verbose_name='Origem')
#     destino = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         verbose_name='Destino')
#     distancia = models.PositiveIntegerField(
#         verbose_name='Distância')
#     descricao = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         verbose_name='Descrição')

#     def __str__(self):
#         return "Origem: " + str(self.origem) + " - Destino: " + str(self.destino) + " - Distância: " + str(self.distancia)+"Km" + " - Descrição: " + str(self.descricao)

#     class Meta:
#         ordering = ['distancia']
#         verbose_name = "Rota do Veículo"
#         verbose_name_plural = "Rotas do Veículo"
