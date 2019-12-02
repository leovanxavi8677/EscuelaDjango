from django.forms import ModelForm
from .models import Grupo

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'numeroAlumnos', 'estatus', 'materia', 'maestroAsignado']
