from django.views.generic import ListView
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


class CadastrarLiberarVeiculo(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = LiberarVeiculo
    fields = ['observacoes', 'agendamento', 'responsavel_liberacao', 'porteiro_saida',
              'porteiro_chegada', 'confirmacao_saida', 'confirmacao_chegada', 'km_saida', 'km_chegada']
    success_message = 'Cadastrado!'
    sweetify_options = {'text': 'Informações da Liberação do Veículo cadastradas com sucesso.',
                        'timer': 2500
                        }
    template_name = 'LiberarVeiculo/cadastrar_liberar_veiculo.html'
    success_url = reverse_lazy('liberarveiculo:listar_liberar_veiculos')

    def get_context_data(self, **kwargs):
        context = super(CadastrarLiberarVeiculo,
                        self).get_context_data(**kwargs)
        context['cadastrar_liberar_veiculo'] = 'active'
        return context


class LiberarVeiculoListView(SweetifySuccessMixin, ListView, LoginRequiredMixin):
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


class LiberarVeiculoEditView(SweetifySuccessMixin, generic.UpdateView, LoginRequiredMixin):
    model = LiberarVeiculo
    form_class = forms.EditLiberarVeiculoForm
    template_name = 'LiberarVeiculo/cadastrar_liberar_veiculo.html'
    success_message = 'Alterado com Sucesso!'
    sweetify_options = {'text': 'Informações da Liberação do Veículo alteradas com sucesso.',
                        'timer': 2500
                        }

    def get_success_url(self):
        return reverse_lazy('liberarveiculo:listar_liberar_veiculos')


@login_required
def liberar_veiculo_delete(request, pk):
    if id:
        LiberarVeiculo.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações da Liberação do Veículo excluídas com \
                                     sucesso.', timer=2500)
    return redirect("liberarveiculo:listar_liberar_veiculos")
