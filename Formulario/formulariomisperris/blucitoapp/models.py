from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    correo = models.EmailField(max_length=30)
    apellido = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)