from django.forms import ModelForm
from .models import Materia

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre',
                  'estatusMateria',
                  'areaEstudio'
                  ]
        required = [
            'nombre',
            'estatusMateria',
            'areaEstudio'
                   ]
