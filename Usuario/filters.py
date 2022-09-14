import django_filters
from django.db.models import Q
from Usuario.models import Usuario


class UsuarioFilter(django_filters.FilterSet):

    texto = django_filters.CharFilter(
        method='filtro_usuario', label="Pesquisar")

    class Meta:
        model = Usuario
        fields = ['texto']

    def filtro_usuario(self, queryset, username, value):
        return queryset.filter(
            Q(username__icontains=value) | Q(email__icontains=value) | Q(
                funcao__icontains=value) | Q(user_type__icontains=value)
        )
