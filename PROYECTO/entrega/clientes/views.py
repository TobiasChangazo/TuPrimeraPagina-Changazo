from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from clientes.models import Cliente

def nuevo_cliente(request):
    
    print(request.POST)
    
    if request.method == "POST":
        nuevo_cliente = Cliente(
            Nombre = request.POST["Nombre"],
            Apellido = request.POST["Apellido"],
            DNI = request.POST["DNI"]
        )
        nuevo_cliente.save()
        return render(request, 'index.html')
    
    return render(request, 'cliente_formulario.html')