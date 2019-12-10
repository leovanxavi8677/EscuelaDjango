from django.forms import ModelForm
from .models import Estudiante
from django.forms.widgets import DateInput

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
                    'matricula',
                    'numeroMateriasCursando',
                     'totalNumeroMateriasAprobadas',
                    'totalNumerosMateriasReprobadas',
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
