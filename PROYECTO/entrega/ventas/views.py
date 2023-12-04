from django.shortcuts import render
from stock.models import Producto

def busqueda_en_bd(request):
    if request.method == "POST":
        busqueda = request.POST["nombre"]
        lista_productos = Producto.objects.filter(nombre__icontains=busqueda)
        
        return render(request, 'busqueda.html', {'lista': lista_productos})
    
    return render(request, 'busqueda.html')

def comprar_producto(request):
    if request.method == "POST":
        busqueda = request.POST["nombre"]
        producto = Producto.objects.get(nombre=busqueda)
        cantidad_compra = int(request.POST["cantidad"])
        producto.cantidad_en_stock = producto.cantidad_en_stock - cantidad_compra
        producto.save()
        
        return render(request, 'comprar_producto.html', {'producto': producto.nombre, 'cantidad_stock': producto.cantidad_en_stock})
    
    return render(request, 'comprar_producto.html')