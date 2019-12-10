from django.forms import ModelForm, ValidationError
from .models import Estudiante
from django.forms.widgets import DateInput
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
                  'nivelAcceso',
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
                  'nivelAcceso',
                  'matricula',
                  'semestre',
                  'numeroMateriasCursando',
                  'totalNumeroMateriasAprobadas',
                  'totalNumerosMateriasReprobadas',
                  'programaEducativo',
                  'materias'
                    ]
        widgets = {
            'fechaNacimiento': DateInput(format= ('%Y-%m-%d'),
                                         attrs={
                                             'placeholder': 'Ingresa la fecha de nacimiento',
                                             'type': 'date',
                                             'data-provide': 'datepicker',
                                             'data-date-format': 'yyyy-mm-dd',
                                         }
                                         )

        }

        def clean(self):
            pattern_letter_and_space= re.compile('[a-zA-z ]+$')
            nombre = self.cleaned_data.get('nombre')
            if pattern_letter_and_space.match(nombre):
                return nombre
            else:
                raise forms.ValidationError("No es un nombre Valido")