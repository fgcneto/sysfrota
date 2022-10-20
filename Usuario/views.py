from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def home_authenticated(request):
    # user Administrativo
    if request.user.user_type == 1:
        return render(request, "Base/base.html")
    # user Motorista
    elif request.user.user_type == 2:
        return redirect("liberarveiculo:listar-liberar-veiculos-porteiro")
    # user porteiro
    elif request.user.user_type == 3:
        return redirect("liberarveiculo:listar-liberar-veiculos-porteiro")


# @login_required
# def usuario_edit(request, pk):
#     template_name = 'Usuario/cadastrar_usuario.html'
#     usuario = Usuario.objects.get(id=pk)
#     usuario_form = forms.UsuarioForm(request.POST or None, instance=usuario)

#     if request.method == 'POST':
#         if usuario_form.is_valid():
#             usuario_form.save()
#             sweetify.success(request, 'Cadastro Salvo', text='Informações \
#                  do Usuário salvas com sucesso!', timer=3000)
#             return redirect('usuario:listar_usuarios')

#     context = {
#         'usuario_form': usuario_form
#     }

#     return render(request, template_name, context)

class UsuarioEditView(SweetifySuccessMixin, generic.UpdateView, LoginRequiredMixin):
    model = Usuario
    fields = ['is_superuser', 'is_staff', 'user_type',
              'first_name', 'last_name', 'username', 'password',
              'email', 'cpf', 'matricula', 'habilitacao']
    success_message = 'Usuário Alterado com Sucesso!'
    template_name = 'Usuario/editar_usuario.html'
    success_message = 'Editado!'
    sweetify_options = {'text': 'Informações do Usuário alteradas com sucesso!',
                        'timer': 3000
                        }
    template_name = 'Usuario/cadastrar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')

    def get_success_url(self):
        return reverse_lazy("usuario:listar_usuarios")


# @login_required
# def usuario_create(request):
#     template_name = 'Usuario/cadastrar_usuario.html'
#     usuario_form = forms.UsuarioForm(request.POST or None)

#     if request.method == 'POST':
#         if usuario_form.is_valid():
#             usuario_form.save()
#             sweetify.success(request, 'Cadastro Salvo', text='Informações \
#                  do usuário salvas com sucesso!', timer=3000)
#             return redirect('usuario:listar_usuarios')

#     context = {
#         'usuario_form': usuario_form
#     }

#     return render(request, template_name, context)


@login_required
def usuario_delete(request, pk):
    user = Usuario.objects.get(id=pk)

    if id and user.is_active == True:
        user.is_active = False
        user.save()
        sweetify.info(request, 'Cadastro Desativado ',
                      text='Informações do Usuário desativadas com \
                                     sucesso.', timer=3000)
    elif user.is_active == False:
        user.is_active = True
        user.save()
        sweetify.success(request, 'Cadastro Ativado ',
                         text='Informações do Usuário Ativadas com \
                                sucesso.', timer=3000)

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


class UsuarioRegisterView(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = Usuario
    fields = ['is_superuser', 'is_staff', 'user_type',
              'first_name', 'last_name', 'username', 'password',
              'email', 'cpf', 'matricula', 'habilitacao']
    success_message = 'Cadastrado!'
    sweetify_options = {'text': 'Informações do Usuário cadastradas com sucesso.',
                        'timer': 3000
                        }
    template_name = 'Usuario/cadastrar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')

    def get_context_data(self, **kwargs):
        context = super(UsuarioRegisterView, self).get_context_data(**kwargs)
        context['cadastrar_usuario'] = 'active'
        return context
