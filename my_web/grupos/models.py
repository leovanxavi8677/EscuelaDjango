from django.db import models
from ..materias.models import Materia
from ..maestros.models import Maestro
from django.core.validators import validate_integer, validate_slug

ESTATUS_CHOICES=[
    ('1', 'Alta'),
    ('2', 'Baja'),
    ('3', 'Suspendido')
]

class Grupo(models.Model):
    nombre = models.CharField(max_length=60, blank=False, null=False, validators=[validate_slug])
    numeroAlumnos = models.CharField(max_length=2,blank=False, null=False, validators=[validate_integer])
    estatus = models.CharField(max_length=1, blank=False, null=False, choices=ESTATUS_CHOICES)
    materia = models.ForeignKey(Materia, related_name="gruposMaterias", on_delete=models.CASCADE, null=True,
                                help_text="Selecione una Materia")
    maestroAsignado = models.ForeignKey(Maestro, related_name="gruposMaestro", on_delete=models.CASCADE, null=True,help_text="Seleccione un Maestro")

    def __str__(self):
        return "{}".format(self.nombre)

    @property
    def get_nombre_grupo(self):
        return "{}".format(self.nombre)

    @property
    def get_numero_alumnos(self):
        return "{}".format(self.numeroAlumnos)

    @property
    def get_estatus(self):
        if self.estatus == '1':
            return "Alta"
        if self.estatus == '2':
            return "Baja"
        if self.estatus == '3':
            return "Suspendido"

    @property
    def get_materia_grupo(self):
        return "{}".format(self.materia)

    @property
    def get_maestro_asignado(self):
        return "{}".format(self.maestroAsignado)

