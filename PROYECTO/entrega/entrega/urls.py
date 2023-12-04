from django.contrib import admin
from django.urls import path, include
from . import views
from entrega.views import inicio
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('stock',views.stock),
    path('clientes',views.clientes),
    path('ventas',views.ventas),
    
    # URLs de apps
    path('stock/', include('stock.urls')),
    path('clientes/', include('clientes.urls')),
    path('ventas/', include('ventas.urls')),
    
]