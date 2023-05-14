from django.db import models
from django.utils import timezone

class Persona(models.Model):
    TIPO_VIVIENDA = [
        (1, 'Casa con patio grande'),
        (2, 'Casa con patio pequeño'),
        (3, 'Casa sin patio'),
        (4, 'Departamento'),

    ]
    correo_electronico = models.EmailField()
    rut = models.CharField(max_length=10,verbose_name='Rut')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    telefono = models.CharField(max_length=15,verbose_name='Telefono')
    cuidad = models.CharField(max_length=50,verbose_name='Cuidad')
    vivienda = models.IntegerField(choices=TIPO_VIVIENDA)

def __str__(self):
    return self.nombre



