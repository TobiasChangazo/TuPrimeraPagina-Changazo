from django import forms

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    unidad_de_medida = forms.CharField()
    cantidad_en_stock = forms.IntegerField()