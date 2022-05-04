
from django.urls import path
from core.views.category.views import *
from core.views.producto.views import *
from core.views.dashboard.views import *
from core.views.cliente.views import *


urlpatterns = [
    #Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    path('category/dashboard/', DashboardView.as_view(), name='category_dashboard'),
    #Producto
    path('product/list/', ProductListView.as_view(), name='list_product'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    #Cliente
    path('client/list/', ClientListView.as_view(), name='list_client'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),


    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
