import django_filters
from django.db.models import Q
from .models import LiberarVeiculo


class LiberarVeiculoFilter(django_filters.FilterSet):

    texto = django_filters.CharFilter(
        method='filtro_liberar_veiculo', label="Pesquisar")

    class Meta:
        model = LiberarVeiculo
        fields = ['texto']

    def filtro_liberar_veiculo(self, queryset, value):
        return queryset.filter(
            Q(data_hora_saida__icontains=value) | Q(
                data_hora_chegada__icontains=value)
        )
