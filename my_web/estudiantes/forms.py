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
            'fechaNacimiento': DateInput(format= ('%Y-%m-%d'),
                                         attrs={
                                             'placeholder': 'Ingresa la fecha de nacimiento',
                                             'type': 'date',
                                             'data-provide': 'datepicker',
                                             'data-date-format': 'yyyy-mm-dd',
                                         }
                                         )

        }
        """
        def clean_nombre(self):
            nombre = self.cleaned_data['nombre']
            if not nombre.isalpha():
                raise forms.ValidationError('Primero nombre debe contener solo letras')
            return nombre
        """

        def clean_matricula(self):
            matricula= self.cleaned_data.get('matricula')
            for instance in Estudiante.objects.all():
                if instance.matricula == matricula:
                    raise forms.ValidationError('Ya existe una matricula {}'.format(
                        matricula
                    ))
            return matricula

        def clean_nombre(self):
            pattern_letter_and_space = re.compile('[a-zA-z ]+$')
            nombre = self.cleaned_data.get('nombre')
            if pattern_letter_and_space.match(nombre):
                pass
            else:
                raise forms.ValidationError("No es un nombre Valido")
