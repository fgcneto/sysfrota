from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from Agenda.models import Agenda
from Agenda.filters import AgendaFilter
from Agenda import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


class AgendaRegisterView(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = Agenda
    fields = ['descricao', 'data_saida', 'data_retorno', 'hora_saida',
              'hora_retorno', 'veiculo', 'motorista', 'usuario_cadastro']
    success_message = 'Cadastrado!'
    sweetify_options = {'text': 'Informações do Agendamento cadastradas com sucesso.',
                        'timer': 2500
                        }
    template_name = 'Agenda/cadastrar_agendamento.html'
    success_url = reverse_lazy('agenda:listar_agendamentos')

    def get_context_data(self, **kwargs):
        context = super(AgendaRegisterView, self).get_context_data(**kwargs)
        context['cadastrar_agendamento'] = 'active'
        return context


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
                        'timer': 2500
                        }

    def get_success_url(self):
        return reverse_lazy('agenda:listar_agendamentos')


@login_required
def agendamento_delete(request, pk):
    if id:
        Agenda.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Agendamento excluídas com \
                                     sucesso.', timer=2000)
    return redirect("agenda:listar_agendamentos")
