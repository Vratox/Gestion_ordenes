from django import forms
from ordenes.models import Orden

class Orden_forms(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['titulo', 'descripcion']
        