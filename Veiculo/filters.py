import django_filters
from django.db.models import Q
from Veiculo.models import Veiculo


class VeiculoFilter(django_filters.FilterSet):

    texto = django_filters.CharFilter(
        method='filtro_veiculo', label="Pesquisar")

    class Meta:
        model = Veiculo
        fields = ['texto']

    def filtro_veiculo(self, queryset, name, value):
        return queryset.filter(
            Q(marca__icontains=value) | Q(placa__icontains=value) | Q(
                modelo__icontains=value) | Q(ano_fabricacao__icontains=value)
        )
