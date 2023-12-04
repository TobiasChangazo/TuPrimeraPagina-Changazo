from django.urls import path
from ventas.views import comprar_producto, busqueda_en_bd

urlpatterns = [
    path('comprar_producto/', comprar_producto),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda en bd'),
    path('comprar_producto/', comprar_producto, name='comprar producto'),
]