from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone
from core.choices import gender_choices
# Create your models here.
class Type(models.Model): # --- CREACION MODELO TIPO ---
    name = models.CharField(verbose_name='Nombre', max_length=50,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural = 'Tipos'
        ordering=['id']

class Employee(models.Model): #---CREADION DE UNA CLASE EMPLEADO---
    type= models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(verbose_name='Nombres', max_length=50,)
    apellido = models.CharField(verbose_name='Nombres', max_length=50,)
    dni = models.IntegerField(verbose_name='Dni', unique=True,)
    date_joined = models.DateField(verbose_name= 'Fecha de Registro', default= datetime.now)
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now_add=True)
    salary = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural = 'Empleados'
        db_table= 'empleado'
        ordering=['id']

class Category(models.Model): # --- CREACION DE UNA CATEGORIA ---
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null= True, blank= True, verbose_name= 'Descripcion')

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model): # --- CREACION DE UN PRODUCTO ---
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']