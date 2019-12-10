from django.forms import ModelForm
from .models import Maestro
from django.forms.widgets import DateInput

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
                                         }
                                         )

        }