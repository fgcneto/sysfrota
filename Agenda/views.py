from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy
from Agenda.models import Agenda
from Agenda.filters import AgendaFilter

import sweetify
from sweetify.views import SweetifySuccessMixin


class AgendaRegisterView(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = Agenda
    fields = ['descricao', 'data_saida', 'data_retorno', 'hora_saida',
              'hora_retorno', 'rotas_veiculos', 'veiculo', 'motorista', 'usuario_cadastro']
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
