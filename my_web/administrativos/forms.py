from django.forms import ModelForm
from .models import Administrativo
from django.forms.widgets import TextInput, DateInput

class AdministrativoForm(ModelForm):
    class Meta:
        model = Administrativo
        fields = ['nombre',
                  'apellidoPaterno',
                  'apellidoMaterno',
                  'fechaNacimiento',
                  'edad',
                  'nivelEstudios',
                  'genero',
                  'numeroAdministrativo',
                  'numeroOficina',
                  ]

        required = ['nombre',
                  'apellidoPaterno',
                  'apellidoMaterno',
                  'fechaNacimiento',
                  'edad',
                  'nivelEstudios',
                  'genero',
                  'numeroAdministrativo',
                  'numeroOficina',
                  ]

        widgets = {
            'fechaNacimiento': DateInput(format=('%Y-%m-%d'),
                                         attrs={
                                             'placeholder': 'Ingresa la fecha de nacimiento',
                                             'type': 'date',
                                             'data-provide': 'datepicker',
                                             'data-date-format': 'yyyy-mm-dd',
                                         }),
            'numeroAdministrativo': TextInput(attrs={
                'class': 'md-form',
                'id': 'txt_numeroAdministrativo',
                'name': 'txt_numeroAdministrativo',
                'onKeyPress': 'return lettersAndNumbers(event)',

            }),
            'numeroOficina': TextInput(attrs={
                'class': 'md-form',
                'id': 'txt_numeroOficina',
                'name': 'txt_numeroOficina',
                'onkeypress': 'return isNumberKey(event);',
            })
        }