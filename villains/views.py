# villains/views.py
from django.shortcuts import render
from .models import Villain
from .forms import VillainForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class VillainListView(ListView):
    model = Villain
    template_name = "villains/lista_viloes.html"
    context_object_name = "viloes"

class CreateVillain(CreateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_vilao.html'
    success_url = reverse_lazy('lista_viloes')
    
class UpdateVillain(UpdateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_vilao.html'
    success_url = reverse_lazy('lista_viloes')

class DeleteVillain(DeleteView):
    model = Villain
    template_name = 'villains/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_viloes')

