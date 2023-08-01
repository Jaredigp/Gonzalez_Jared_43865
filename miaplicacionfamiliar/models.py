from django.db import models

# Create your models here.
class Familia(models.Model):
    apellido_primero = models.CharField(max_length=30)
    apellido_segundo = models.CharField(max_length=30)
    estado_residencia = models.CharField(max_length=30)
    ciudad_residencia = models.CharField(max_length=30)

class Ascendencia(models.Model):
    apellido_primero = models.CharField(max_length=30)
    apellido_segundo = models.CharField(max_length=30)
    nombre_padre = models.CharField(max_length=30)
    nombre_madre = models.CharField(max_length=30)

class Ocupacion(models.Model):
    nivel_estudios = models.CharField(max_length=30)
    puesto = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    maestria = models.BooleanField()