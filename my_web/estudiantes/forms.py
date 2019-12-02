from django.forms import ModelForm
from .models import Estudiante

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'edad', 'nivelEstudios',
                  'genero', 'nivelAcceso', 'matricula', 'semestre', 'numeroMateriasCursando', 'totalNumeroMateriasAprobadas',
                  'totalNumerosMateriasReprobadas', 'programaEducativo', 'materias']
