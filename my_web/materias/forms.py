from django import forms

class MateriaForm(forms.Form):
    nombre = forms.CharField(label="Nombre Materia", max_length=30, strip=True)