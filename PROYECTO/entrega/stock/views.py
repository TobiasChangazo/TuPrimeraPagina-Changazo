from django.shortcuts import render
from stock.models import Producto
from django.template import loader
from django.http import HttpResponse

def ingresar_producto(request):    
    
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        
        nuevo_producto.save()
        return render(request, 'index.html')
    
    return render(request, 'producto_formulario.html')
