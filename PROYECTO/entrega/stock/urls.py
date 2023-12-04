from django.urls import path
from stock.views import ingresar_producto

urlpatterns = [
    path('ingresar_producto/', ingresar_producto, name='ingresar producto'),
]