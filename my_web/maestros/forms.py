from django.forms import ModelForm
from .models import Maestro
from django.forms.widgets import DateInput
from django.forms.widgets import DateInput, TextInput, Select, SelectMultiple, NumberInput

class MaestroForm(ModelForm):
    class Meta:
        model = Maestro
        fields = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'fechaNacimiento',
            'edad',
            'nivelEstudios',
            'genero',
            'cubiculo',
            'numeroTrabajador',
            'estatus',
            'areamaestro',
        ]
        required = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'fechaNacimiento',
            'edad',
            'nivelEstudios',
            'genero',
            'cubiculo',
            'numeroTrabajador',
            'estatus',
            'areamaestro',

        ]
        widgets = {
            'fechaNacimiento': DateInput(format= ('%Y-%m-%d'),
                                         attrs={
                                             'placeholder': 'Ingresa la fecha de nacimiento',
                                             'type': 'date',
                                             'data-provide': 'datepicker',
                                             'data-date-format': 'yyyy-mm-dd',
                                         } ),
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
            'edad': TextInput(attrs={
                'class': 'txt_edad',
                'id': 'txt_edad',
                'name': 'txt_edad',
                'onkeypress': 'return isNumberKey(event);',

            }),
            'nivelEstudios': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'genero': Select(attrs={
                'class': 'custom-select mr-sm-2'
            }),
            'cubiculo': TextInput(attrs={
                'class': 'txt_cubiculo',
                'id': 'txt_cubiculo',
                'name': 'txt_cubiculo',
                'onkeypress': ' return lettersAndNumbers(event);',

            }),
            'numeroTrabajador': TextInput(attrs={
                'class': 'txt_numeroTrabajador',
                'id': 'txt_numeroTrabajador',
                'name': 'txt_numeroTrabajador',
                'onkeypress': ' return lettersAndNumbers(event);',

            }),
            'estatus': Select(attrs={
                'class': 'custom-select mr-sm-2'

            }),
            'areamaestro': Select(attrs={
                'class': 'custom-select mr-sm-2'

            })

        }