from django.forms import ModelForm
from .models import Maestro

class MaestroForm(ModelForm):
    class Meta:
        model = Maestro
        fields = [
            'nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'edad', 'nivelEstudios', 'genero',
            'nivelAcceso', 'cubiculo', 'numeroTrabajador', 'estatus', 'areamaestro',
        ]
