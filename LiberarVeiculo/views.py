from django.views.generic import ListView
from django.utils.timezone import now
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from LiberarVeiculo.models import LiberarVeiculo
from LiberarVeiculo.filters import LiberarVeiculoFilter
from LiberarVeiculo import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


class CadastrarLiberarVeiculo(LoginRequiredMixin, generic.CreateView, SweetifySuccessMixin):
    model = LiberarVeiculo
    form_class = forms.LiberarVeiculoForm
    fields = ['observacoes', 'agendamento'
              ]
    success_message = 'Cadastrado!'
    sweetify_options = {'text': 'Informações da Liberação do Veículo cadastradas com sucesso.',
                        'timer': 2500
                        }
    template_name = 'LiberarVeiculo/cadastrar_liberar_veiculo.html'
    success_url = reverse_lazy('liberarveiculo:listar_liberar_veiculos')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.responsavel_liberacao = self.request.user
        self.object.save()
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        if success_message:
            sweetify.success(self.request, success_message,
                             **self.get_sweetify_options())
            return response
        else:
            sweetify.error(self.request, 'Erro ao editar',
                           text='Erro ao Editar a Liberação deste Veículo', timer=3000)
            return redirect("liberarveiculo:listar_liberar_veiculos")

    def get_context_data(self, **kwargs):
        context = super(CadastrarLiberarVeiculo,
                        self).get_context_data(**kwargs)
        context['cadastrar_liberar_veiculo'] = 'active'
        return context

    def get_form_class(self):
        return self.form_class

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options


class LiberarVeiculoListView(LoginRequiredMixin, ListView, SweetifySuccessMixin):
    model = LiberarVeiculo
    paginate_by = 6
    template_name = 'LiberarVeiculo/listar_liberar_veiculos.html'
    context_object_name = 'liberarveiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = LiberarVeiculoFilter(
            self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super(LiberarVeiculoListView,
                        self).get_context_data(**kwargs)
        context['liberarveiculos'] = LiberarVeiculo.objects.all()
        context['listar_liberar_veiculos'] = 'active'
        context['filterset'] = self.filterset
        return context


class LiberarVeiculoEditView(LoginRequiredMixin, generic.UpdateView, SweetifySuccessMixin):
    model = LiberarVeiculo
    form_class = forms.LiberarVeiculoForm
    template_name = 'LiberarVeiculo/cadastrar_liberar_veiculo.html'
    success_message = 'Alterado com Sucesso!'
    sweetify_options = {'text': 'Informações da Liberação do Veículo alteradas com sucesso.',
                        'timer': 2500
                        }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.responsavel_liberacao = self.request.user
        self.object.save()
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        if success_message:
            sweetify.success(self.request, success_message,
                             **self.get_sweetify_options())
            return response
        else:
            sweetify.error(self.request, 'Erro ao editar',
                           text='Erro ao Editar a Liberação deste Veículo', timer=3000)
            return redirect("liberarveiculo:listar_liberar_veiculos")

    def get_form_class(self):
        return self.form_class

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options

    def get_success_url(self):
        return reverse_lazy('liberarveiculo:listar_liberar_veiculos')


class LiberarVeiculoPorteiroEditView(LoginRequiredMixin, generic.UpdateView, SweetifySuccessMixin):
    model = LiberarVeiculo
    form_class = forms.LiberarVeiculoPorteiroForm
    template_name = 'LiberarVeiculo/cadastrar_liberar_veiculo_porteiro.html'
    success_message = 'Alterado com Sucesso!'
    sweetify_options = {'text': 'Informações da Liberação do Veículo alteradas com sucesso.',
                        'timer': 2500
                        }

    def form_valid(self, form):
        hora_atual = now()
        self.object = form.save(commit=False)

        if self.object.porteiro_saida == None:
            self.object.confirmacao_saida = True
            self.object.porteiro_saida = self.request.user
            self.object.data_hora_saida = hora_atual
        elif self.object.porteiro_chegada == None:
            self.object.confirmacao_chegada = True
            self.object.porteiro_chegada = self.request.user
            self.object.data_hora_chegada = hora_atual

        self.object.save()
        response = super(SweetifySuccessMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        if success_message:
            sweetify.success(self.request, success_message,
                             **self.get_sweetify_options())
            return response
        else:
            sweetify.error(self.request, 'Erro ao editar',
                           text='Erro ao Editar a Liberação deste Veículo', timer=3000)
            return redirect("liberarveiculo:listar-liberar-veiculos-porteiro")

    def get_form_class(self):
        return self.form_class

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options

    def get_success_url(self):
        return reverse_lazy('liberarveiculo:listar-liberar-veiculos-porteiro')


@login_required
def liberar_veiculo_delete(request, pk):
    if id:
        LiberarVeiculo.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da Liberação do Veículo excluídas com \
                                     sucesso.', timer=2500)
    return redirect("liberarveiculo:listar_liberar_veiculos")


class LiberarVeiculoPorteiroListView(LoginRequiredMixin, ListView, SweetifySuccessMixin):
    model = LiberarVeiculo
    paginate_by = 6
    template_name = 'LiberarVeiculo/listar_liberar_veiculos_porteiro.html'
    context_object_name = 'liberarveiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = LiberarVeiculoFilter(
            self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        liberacoes_veiculos = LiberarVeiculo.objects.all()
        agenda_atual = []

        for liberacao in liberacoes_veiculos:
            agenda_atual.append(liberacao)

        context = super(LiberarVeiculoPorteiroListView,
                        self).get_context_data(**kwargs)
        context['liberarveiculos'] = agenda_atual
        context['listar_agendamentos'] = 'active'
        context['filterset'] = self.filterset
        return context
