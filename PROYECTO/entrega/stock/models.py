from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()