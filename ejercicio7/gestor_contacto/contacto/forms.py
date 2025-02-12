from django import forms
from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'celular', 'email', 'direccion']