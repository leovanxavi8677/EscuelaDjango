from django.db import models
from ..materias.models import Materia
from ..maestros.models import Maestro

ESTATUS_CHOICES=[
    ('1', 'Alta'),
    ('2', 'Baja'),
    ('3', 'Suspendido')
]

class Grupo(models.Model):
    nombre = models.CharField(max_length=60, blank=False, null=False)
    numeroAlumnos = models.PositiveSmallIntegerField(blank=False, null=False)
    estatus = models.CharField(max_length=1, blank=False, null=False, choices=ESTATUS_CHOICES)
    materia = models.ForeignKey(Materia, related_name="gruposMaterias", on_delete=models.CASCADE, null=True,
                                help_text="Selecione una Materia")
    #maestroAsignado = models.ForeignKey(Maestro, related_name="gruposMaestro", on_delete=models.CASCADE, null=True,help_text="Seleccione un Maestro")

    def __str__(self):
        return "{}".format(self.nombre)

