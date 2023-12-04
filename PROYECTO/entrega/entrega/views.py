from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio(request):
    return render(request, "index.html")

def stock(request):
    return render(request, 'producto_formulario.html')

def clientes(request):
    return render(request, 'cliente_formulario.html')

def ventas(request):
    return render(request, 'lista_productos.html')

def comprar_producto(request):
    return render(request, 'comprar_producto.html')