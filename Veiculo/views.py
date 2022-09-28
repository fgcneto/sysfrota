from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from Veiculo.models import Veiculo
from Veiculo.filters import VeiculoFilter
from Veiculo import forms

import sweetify
from sweetify.views import SweetifySuccessMixin


@login_required
def veiculo_create(request):
    template_name = 'Veiculo/cadastrar_veiculo.html'
    veiculo_form = forms.VeiculoForm(request.POST or None)

    if request.method == 'POST':
        if veiculo_form.is_valid():
            veiculo_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do veiculo salvas com sucesso!', timer=3000)
            return redirect('veiculo:listar_veiculos')

    context = {
        'veiculo_form': veiculo_form
    }

    return render(request, template_name, context)


@login_required
def veiculo_edit(request, pk):
    template_name = 'Veiculo/cadastrar_veiculo.html'
    veiculo = Veiculo.objects.get(id=pk)
    veiculo_form = forms.VeiculoForm(request.POST or None, instance=veiculo)

    if request.method == 'POST':
        if veiculo_form.is_valid():
            veiculo_form.save()
            sweetify.success(request, 'Cadastro Salvo', text='Informações \
                 do Veículo salvas com sucesso!', timer=3000)
            return redirect('veiculo:listar_veiculos')

    context = {
        'veiculo_form': veiculo_form
    }

    return render(request, template_name, context)


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


@login_required
def veiculo_delete(request, pk):
    if id:
        Veiculo.objects.filter(id=pk).delete()
        sweetify.success(request, 'Cadastro Excluído ',
                         text='Informações do Veículo excluídas com \
                                     sucesso.', timer=2000)
    return redirect("veiculo:listar_veiculos")
