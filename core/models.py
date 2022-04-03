from datetime import datetime
from django.db import models

# Create your models here.
class Employee(models.Model): #---CREADION DE UNA CLASE EMPLEADO---
    name = models.CharField('Nombre', max_length=50,)
    apellido = models.CharField('Apellido', max_length=50,)
    dni = models.IntegerField('Dni', max_length=8, unique=True,)
    date_joined = models.DateField('Fecha Registro', auto_now= datetime.now,)
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



