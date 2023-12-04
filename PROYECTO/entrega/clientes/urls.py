from django.urls import path
from clientes.views import nuevo_cliente

urlpatterns = [
    path('nuevo_cliente/', nuevo_cliente, name='nuevo_cliente'),
]