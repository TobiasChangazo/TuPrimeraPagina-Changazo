from django import forms

class ClienteFormulario(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    DNI = forms.CharField()