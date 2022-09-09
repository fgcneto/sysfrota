from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings

from Usuario.models import Usuario
from Usuario.filters import UsuarioFilter
from Usuario import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


def home(request):

    if request.user.is_authenticated:
        return home_authenticated(request)
    else:
        return home_logout(request)


def home_logout(request):
    if not request.user.is_authenticated:
        #  return render(request, 'myapp/login_error.html)
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def home_authenticated(request):
    return render(request, "Base/base.html")


class UsuarioEditView(SweetifySuccessMixin, generic.UpdateView, LoginRequiredMixin):
    model = Usuario
    form_class = forms.EditUsuarioForm
    success_message = 'Usuário Alterado com Sucesso!'
    template_name = 'Usuario/editar_usuario.html'

    def get_success_url(self):
        return reverse_lazy("usuario:listar_usuarios")


class UsuarioDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Usuario
    success_url = reverse_lazy("usuario:listar_usuarios")


@login_required
def usuario_delete(request, pk):  # deletar essa função
    print(Usuario.objects.filter(id=pk))

    #     if id:
    #         print(Usuario.objects.filter(id=pk).delete())
    #         Usuario.objects.filter(id=pk).delete()
    #         sweetify.success(request, 'Cadastro Excluído ',
    #                          text='Informações do Usuário excluídas com \
    #                                  sucesso.', timer=1500)
    return redirect("usuario:listar_usuarios")


class UsuarioListView(ListView, LoginRequiredMixin):
    model = Usuario
    paginate_by = 6
    template_name = 'Usuario/listar_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UsuarioFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super(UsuarioListView, self).get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['listar_usuarios'] = 'active'
        context['filterset'] = self.filterset
        return context
