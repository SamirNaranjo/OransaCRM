from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.urls import reverse_lazy
from core.models import Client
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.forms import *


class ClientListView(ListView):
    model = Client
    template_name = 'list_client.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Client.objects.all()

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado De Clientes'
        context['create_url'] = reverse_lazy('client_create')
        context['list_url'] = reverse_lazy('list_client')
        context['entity'] = 'Client'
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'create_client.html'
    success_url = reverse_lazy('list_client')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


          
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Un Cliente'
        context['entity'] = 'Client'
        context['list_url'] = reverse_lazy('list_client')
        context['action'] = 'add'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'create_client.html'
    success_url = reverse_lazy('list_client')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Cliente'
        context['entity'] = 'Client'
        context['list_url'] = reverse_lazy('list_client')
        context['action'] = 'edit'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "delete_client.html"
    success_url = reverse_lazy('list_client')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Cliente'
        context['entity'] = 'Client'
        context['list_url'] = reverse_lazy('list_client')
        return context