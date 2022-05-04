from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.urls import reverse_lazy
from core.models import Product
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.forms import *


class ProductListView(ListView):
    model = Product
    template_name = 'list_product.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Product.objects.all()

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado De Productos'
        context['create_url'] = reverse_lazy('product_create')
        context['list_url'] = reverse_lazy('list_product')
        context['entity'] = 'productos'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('list_product')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


          
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Un Producto'
        context['entity'] = 'productos'
        context['list_url'] = reverse_lazy('list_product')
        context['action'] = 'add'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('list_product')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Producto'
        context['entity'] = 'productos'
        context['list_url'] = reverse_lazy('list_product')
        context['action'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy('list_product')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Producto'
        context['entity'] = 'productos'
        context['list_url'] = reverse_lazy('list_product')
        return context

# class ProductFormView(FormView):
#     form_class= ProductForm
#     template_name='create_product.html'
#     success_url = reverse_lazy('list_product')

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def form_invalid(self, form): 
#         return super().form_invalid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Form | Producto'
#         context['entity'] = 'productos'
#         context['list_url'] = reverse_lazy('list_product')
#         context['action'] = 'add'
#         return context
