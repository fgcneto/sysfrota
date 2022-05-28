from django.contrib import admin
from Usuario.models import Administrador, Motorista, Porteiro

admin.site.register(Administrador)
admin.site.register(Porteiro)
admin.site.register(Motorista)
