from django.db import models

# Create your models here.

class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.TextField()
    DNI = models.IntegerField()