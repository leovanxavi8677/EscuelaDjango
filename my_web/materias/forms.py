from django.forms import ModelForm
from .models import Materia
from django.forms.widgets import DateInput, TextInput, Select, SelectMultiple, NumberInput

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
        widgets = {
               'nombre': TextInput(attrs={
                'class': 'txt_nombre',
                'id': 'txt_nombre',
                'name': 'txt_nombre',
                'onkeypress': ' return lettersAndNumbers(event);',

            }),
            'estatusMateria': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'areaEstudio': Select(attrs={
                'class': 'custom-select mr-sm-2'
            })
        }
