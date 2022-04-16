from django.contrib import admin
from django.urls import path
from .views import prueba

urlpatterns = [
    path('prueba/', prueba),
]
