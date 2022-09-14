import django_filters
from django.db.models import Q
from .models import Agenda


class AgendaFilter(django_filters.FilterSet):

    texto = django_filters.CharFilter(
        method='filtro_agenda', label="Pesquisar")

    class Meta:
        model = Agenda
        fields = ['texto']

    def filtro_agenda(self, queryset, name, value):
        return queryset.filter(
            Q(data_saida__icontains=value) | Q(data_retorno__icontains=value)
        )
