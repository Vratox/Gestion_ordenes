from django import forms
from cliente.models import Cliente

class Cliente_forms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe su nombre'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su correo'})
        }