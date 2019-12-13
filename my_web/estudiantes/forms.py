from django.forms import ModelForm, ValidationError
from .models import Estudiante
from django.forms.widgets import DateInput, TextInput, Select, SelectMultiple, NumberInput

import re
from django import forms

class EstudianteForm(ModelForm):



    class Meta:
        model = Estudiante
        fields = ['nombre',
                  'apellidoPaterno',
                  'apellidoMaterno',
                  'fechaNacimiento',
                  'edad',
                  'nivelEstudios',
                  'genero',
                  'matricula',
                  'semestre',
                  'numeroMateriasCursando',
                  'totalNumeroMateriasAprobadas',
                  'totalNumerosMateriasReprobadas',
                  'programaEducativo',
                  'materias'
                  ]
        required = ['nombre',
                  'apellidoPaterno',
                  'apellidoMaterno',
                  'fechaNacimiento',
                  'edad',
                  'nivelEstudios',
                  'genero',
                  'matricula',
                  'semestre',
                  'numeroMateriasCursando',
                  'totalNumeroMateriasAprobadas',
                  'totalNumerosMateriasReprobadas',
                  'programaEducativo',
                  'materias'
                    ]
        widgets = {
            'nombre': TextInput(attrs={
                'class': 'txt_nombre',
                'id': 'txt_nomnbre',
                'name': 'txt_nombre',
                'onKeyPress': 'return ValidateAlpha(event);',

            }),
            'apellidoPaterno': TextInput(attrs={
                'class': 'txt_apellidoPaterno',
                'id': 'txt_apellidoPaterno',
                'name': 'txt_apellidoPaterno',
                'onKeyPress': 'return ValidateAlpha(event);',

            }),

            'apellidoMaterno': TextInput(attrs={
                'class': 'txt_apellidoMaterno',
                'id': 'txt_apellidoMaterno',
                'name': 'txt_apellidoMaterno',
                'onKeyPress': 'return ValidateAlpha(event);',

            }),
            'edad': NumberInput(attrs={
                'class': 'txt_edad',
                'id': 'txt_edad',
                'name': 'txt_edad',
                'onkeypress': 'return isNumberKey(event);',

            }),
            'matricula': NumberInput(attrs={
                'class': 'txt_matricula',
                'id': 'txt_matricula',
                'name': 'txt_matricula',
                'onkeypress': ' return lettersAndNumbers(event);',

            }),
            'numeroMateriasCursando': TextInput(attrs={
                'class': 'txt_numeroMateriasCursando',
                'id': 'txt_numeroMateriasCursando',
                'name': 'txt_numeroMateriasCursando',
                'onkeypress': 'return isNumberKey(event);',

            }),
            'totalNumeroMateriasAprobadas': TextInput(attrs={
                'class': 'txt_totalNumeroMateriasAprobadas',
                'id': 'txt_totalNumeroMateriasAprobadas',
                'name': 'txt_totalNumeroMateriasAprobadas',
                'onkeypress': 'return isNumberKey(event);',

            }),
            'totalNumerosMateriasReprobadas': TextInput(attrs={
                'class': 'txt_totalNumerosMateriasReprobadas',
                'id': 'txt_totalNumerosMateriasReprobadas',
                'name': 'txt_totalNumerosMateriasReprobadas',
                'onkeypress': 'return isNumberKey(event);',

            }),
            'materias': Select(

                attrs={
                  'class': 'selectpicker',
                    'id': 'select_materias',
                    'name': 'select_materias',
                    'multiple': 'multiple',
                    'data-selected-text-format': 'count'

            }),
            'nivelEstudios': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'semestre': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'genero': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'programaEducativo': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'fechaNacimiento': DateInput(format= ('%Y-%m-%d'),
                                         attrs={
                                             'placeholder': 'Ingresa la fecha de nacimiento',
                                             'type': 'date',
                                             'data-provide': 'datepicker',
                                             'data-date-format': 'yyyy-mm-dd',
                                         }
                                         )

        }

