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
    # user Motorista
    if request.user.user_type == 2:
        return redirect("liberarveiculo:listar-liberar-veiculos-porteiro")
    # user porteiro
    elif request.user.user_type == 3:
        return redirect("liberarveiculo:listar-liberar-veiculos-porteiro")
        # user Administrativo
    else:
        return render(request, "Base/base.html")


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
    form_class = forms.CustomUserCreationForm
    fields = ['user_type', 'first_name', 'last_name',
              'username', 'password', 'email',
              'cpf', 'matricula', 'habilitacao']
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        response = super(SweetifySuccessMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            sweetify.success(self.request, success_message,
                             **self.get_sweetify_options())
            return response
        else:
            sweetify.error(self.request, 'Erro ao editar',
                           text='Verificar informações cadastrais', timer=3000)
            return redirect("usuario:cadastrar_usuario")

    def get_form_class(self):
        return self.form_class

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options
