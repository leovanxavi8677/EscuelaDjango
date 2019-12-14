from django.forms import ModelForm
from .models import Grupo
from django.forms.widgets import  TextInput, Select, SelectMultiple, NumberInput

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre',
                  'numeroAlumnos',
                  'estatus',
                  'materia',
                  'maestroAsignado'
                  ]

        required = [
                    'nombre',
                    'numeroAlumnos',
                    'estatus',
                    'materia',
                    'maestroAsignado'
                    ]
        widgets = {
            'nombre': TextInput(attrs={
                'class': 'txt_nombre',
                'id': 'txt_nomnbre',
                'name': 'txt_nombre',
                'onKeyPress': 'return ValidateAlpha(event);',

            }),
            'numeroAlumnos': TextInput(attrs={
                'class': 'txt_numeroAlumnos',
                'id': 'txt_numeroAlumnos',
                'name': 'txt_numeroAlumnos',
                'onkeypress': 'return isNumberKey(event);',
                'maxlenght': '2',

            }),
            'estatus': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'materia': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'maestroAsignado': Select(attrs={
                'class': 'custom-select mr-sm-2'
            })
            
        }
