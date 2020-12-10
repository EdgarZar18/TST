from django import forms
from .models import Registro

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
