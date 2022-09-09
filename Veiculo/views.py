from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from Veiculo.models import Veiculo
from Veiculo.filters import VeiculoFilter
from Veiculo import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


class CadastrarVeiculo(SweetifySuccessMixin, generic.CreateView, LoginRequiredMixin):
    model = Veiculo
    fields = ['marca', 'tipo', 'placa', 'kilometragem', 'ano_fabricacao']
    success_message = 'Cadastrado!'
    sweetify_options = {'text': 'Informações do Veículo cadastradas com sucesso.',
                        'timer': 2500
                        }
    template_name = 'Veiculo/cadastrar_veiculo.html'
    success_url = reverse_lazy('veiculo:listar_veiculos')

    def get_context_data(self, **kwargs):
        context = super(CadastrarVeiculo, self).get_context_data(**kwargs)
        context['cadastrar_veiculo'] = 'active'
        return context


class VeiculoListView(SweetifySuccessMixin, ListView, LoginRequiredMixin):
    model = Veiculo
    paginate_by = 6
    template_name = 'Veiculo/listar_veiculos.html'
    context_object_name = 'veiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = VeiculoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super(VeiculoListView, self).get_context_data(**kwargs)
        context['veiculos'] = Veiculo.objects.all()
        context['listar_veiculos'] = 'active'
        context['filterset'] = self.filterset
        return context


class VeiculoEditView(SweetifySuccessMixin, generic.UpdateView, LoginRequiredMixin):
    model = Veiculo
    form_class = forms.EditVeiculoForm
    template_name = 'Veiculo/cadastrar_veiculo.html'
    success_message = 'Alterado com Sucesso!'
    sweetify_options = {'text': 'Informações do Veículo alteradas com sucesso.',
                        'timer': 2500
                        }

    def get_success_url(self):
        return reverse_lazy('veiculo:listar_veiculos')


@login_required
def veiculo_delete(request, pk):
    if id:
        Veiculo.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Veículo excluídas com \
                                     sucesso.', timer=2000)
    return redirect("veiculo:listar_veiculos")
