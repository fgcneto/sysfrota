import re
from django.utils.timezone import now
from datetime import datetime, timedelta
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from Agenda.models import Agenda
from Agenda.filters import AgendaFilter
from Agenda import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


# def verifica_conflito_agendamento_datas(self):
#     agendas = Agenda.objects.all()
#     for agenda in agendas:
#         # se o veículo for igual, verifica o conflito de datas
#         if self.object.veiculo == agenda.veiculo:
#             if self.object.data_saida >= agenda.data_saida \
#                 and self.object.data_saida <= agenda.data_retorno \
#                     and self.object.data_retorno >= agenda.data_saida \
#                     and self.object.data_retorno <= agenda.data_retorno or (self.object.data_retorno >= agenda.data_saida and self.object.data_retorno <= agenda.data_retorno):
#                 return True
#             else:
#                 return False

#         else:
#             return False


class AgendaRegisterView(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = Agenda
    fields = ['descricao', 'data_saida',
              'data_retorno', 'veiculo', 'motorista']
    success_message = 'Cadastrado com Sucesso!'
    sweetify_options = {'text': 'Informações do Agendamento cadastradas com sucesso!',
                        'timer': 3000
                        }
    template_name = 'Agenda/cadastrar_agendamento.html'
    success_url = reverse_lazy('agenda:listar_agendamentos')

    def get_context_data(self, **kwargs):
        context = super(AgendaRegisterView, self).get_context_data(**kwargs)
        context['cadastrar_agendamento'] = 'active'
        return context

    def form_valid(self, form):
        data_atual = now() - timedelta(hours=3)
        self.object = form.save(commit=False)
        self.object.usuario_cadastro = self.request.user
        response = super(SweetifySuccessMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        def verifica_conflito_agendamento_datas(self):
            agendas = Agenda.objects.all()
            for agenda in agendas:
                # se o veículo for igual, verifica o conflito de datas
                if self.object.veiculo == agenda.veiculo:
                    if self.object.data_saida >= agenda.data_saida \
                        and self.object.data_saida <= agenda.data_retorno \
                            and self.object.data_retorno >= agenda.data_saida \
                            and self.object.data_retorno <= agenda.data_retorno or (self.object.data_retorno >= agenda.data_saida and self.object.data_retorno <= agenda.data_retorno):
                        return True
                    else:
                        return False

                else:
                    return False

        if not verifica_conflito_agendamento_datas(self):
            # salvar o agendamento se data_saida for maior que data_retorno
            if self.object.data_saida < self.object.data_retorno and self.object.data_saida >= data_atual:
                self.object.save()
                response = super(SweetifySuccessMixin, self).form_valid(form)
                success_message = self.get_success_message(form.cleaned_data)
                if success_message:
                    sweetify.success(self.request, success_message,
                                     **self.get_sweetify_options())
                return response
        else:
            sweetify.error(self.request, 'Erro ao Cadastrar',
                           text='Já existe outro agendamento dentro deste período', timer=3000)
            return redirect("agenda:listar_agendamentos")

        if self.object.data_saida > self.object.data_retorno \
                or self.object.data_saida == self.object.data_retorno \
                or self.object.data_saida < data_atual:
            sweetify.error(self.request, 'Erro ao cadastrar ',
                           text='Data de saída menor que hoje, igual ou superior a data de retorno', timer=5000)
            return redirect("agenda:cadastrar_agendamento")

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options


class AgendaListView(SweetifySuccessMixin, ListView, LoginRequiredMixin):
    model = Agenda
    paginate_by = 6
    template_name = 'Agenda/listar_agendamentos.html'
    context_object_name = 'agendas'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AgendaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super(AgendaListView, self).get_context_data(**kwargs)
        context['agendas'] = Agenda.objects.all()
        context['listar_agendamentos'] = 'active'
        context['filterset'] = self.filterset
        return context


class AgendaEditView(SweetifySuccessMixin, generic.UpdateView, LoginRequiredMixin):
    model = Agenda
    form_class = forms.EditAgendamentoForm
    template_name = 'Agenda/cadastrar_agendamento.html'
    success_message = 'Alterado com Sucesso!'
    sweetify_options = {'text': 'Informações do Agendamento alteradas com sucesso.',
                        'timer': 3000
                        }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario_cadastro = self.request.user
        data_atual = now() - timedelta(hours=3)

        def verifica_conflito_agendamento_datas(self):
            agendas = Agenda.objects.all()
            for agenda in agendas:
                # se o veículo for igual, verifica o conflito de datas
                print(self.object.veiculo)
                print(agenda.veiculo)
                if self.object.veiculo == agenda.veiculo:
                    if self.object.data_saida >= agenda.data_saida \
                        and self.object.data_saida <= agenda.data_retorno \
                            and self.object.data_retorno >= agenda.data_saida \
                            and self.object.data_retorno <= agenda.data_retorno or (self.object.data_retorno >= agenda.data_saida and self.object.data_retorno <= agenda.data_retorno):
                        return True
                    else:
                        return False

                else:
                    return False

        if not verifica_conflito_agendamento_datas(self):
            # SÓ SALVA o agendamento se data_saida for maior que data retorno
            # E se data de saida for maior ou igual a data atual
            # E se data de retorno for maior ou igual data_atual
            if self.object.data_saida < self.object.data_retorno \
                    and self.object.data_saida >= data_atual:
                self.object.save()
                response = super(SweetifySuccessMixin, self).form_valid(form)
                success_message = self.get_success_message(form.cleaned_data)
                if success_message:
                    sweetify.success(self.request, success_message,
                                     **self.get_sweetify_options())
                return response
        else:
            sweetify.error(self.request, 'Erro ao editar',
                           text='Já existe outro agendamento dentro deste período', timer=3000)
            return redirect("agenda:listar_agendamentos")

        # não permite salvar o agendamento
        if self.object.data_saida >= self.object.data_retorno \
            or self.object.data_saida < data_atual \
                or self.object.data_retorno < data_atual:
            sweetify.error(self.request, 'Erro ao editar ',
                           text='Data de saída menor que hoje, igual ou superior a data de retorno', timer=5000)
            return redirect("agenda:listar_agendamentos")

    def get_error_message(self, errors):
        return self.error_message % errors

    def get_sweetify_options(self):
        return self.sweetify_options

    def get_success_url(self):
        return reverse_lazy('agenda:listar_agendamentos')


@login_required
def agendamento_delete(request, pk):
    agenda = Agenda.objects.get(id=pk)
    if id and not agenda.agendamento_liberacao_veiculo.all():
        Agenda.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Agendamento excluídas com \
                                     sucesso.', timer=3000)
    else:
        sweetify.error(request, 'Erro ao excluir ',
                       text='Este Agendamento já possui uma Liberação cadastrada', timer=3500)
    return redirect("agenda:listar_agendamentos")
