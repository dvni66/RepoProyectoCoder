from django import forms
from AppCoder.models import CATEGORIA, IDIOMA, ESTADO

class PeliForm(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    categoria = forms.ChoiceField(choices=CATEGORIA)
    idioma = forms.ChoiceField(choices=IDIOMA)
    estado = forms.ChoiceField(choices=ESTADO)
    cast = forms.CharField()
    prodYear = forms.DateField()

    def __str__(self):
        return self.titulo

