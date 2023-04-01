from django.db import models

# Create your models here.

class Mascota(models.Model):

    nombre_mascota = models.CharField(max_length=30)
    tipo_de_mascota = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField(max_length=2)
    vacunas = models.CharField(max_length=500)
    comentarios = models.CharField(max_length=2000)
  

class Duenio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mascota = models.CharField(max_length=30)




