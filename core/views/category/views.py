from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.urls import reverse_lazy
from core.models import Category
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.forms import *





class CategoryListView(ListView):
    model = Category
    template_name = 'list_category.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Category.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado De Categorias'
        context['create_url'] = reverse_lazy('category_create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorias'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('category_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'edit'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "delete.html"
    success_url = reverse_lazy('category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        return context

class CategoryFormView(FormView):
    form_class= CategoryForm
    template_name='create.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        return context
