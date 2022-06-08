from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic


class ListarAdministrativo(generic.ListView, LoginRequiredMixin):
    # model = Usuario
    template_name = 'Usuario/Administrativo/listar.html'
    context_object_name = 'listar_administrativo'
