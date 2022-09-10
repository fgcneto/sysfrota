import django_filters
from django.db.models import Q
from .models import LiberarVeiculo


class LiberarVeiculoFilter(django_filters.FilterSet):

    texto = django_filters.CharFilter(
        method='filtro_liberar_veiculo', label="Pesquisar")

    class Meta:
        model = LiberarVeiculo
        fields = ['texto']

    def filtro_liberar_veiculo(self, queryset, name, value):
        return queryset.filter(
            Q(marca__icontains=value) | Q(placa__icontains=value) | Q(
                modelo__icontains=value) | Q(ano_fabricacao__icontains=value)
        )
