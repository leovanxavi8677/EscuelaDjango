from django.db import models
from ..areaestudiomateria.models import AreaEstudioMateria

ESTATUS_MATERIA=[
    ('1', 'Alta'),
    ('2', 'Pendiente'),
    ('3', 'Baja')
]



class Materia(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    estatusMateria = models.CharField(max_length=1, blank=False, null=False, choices=ESTATUS_MATERIA)
    areaEstudio = models.ForeignKey(AreaEstudioMateria, related_name="materiaAreaEstudioMateria",
                                    on_delete=models.CASCADE,null=True,
                                    help_text="Seleccione una Área de Estudio")

    def __str__(self):
        return "{}".format(self.nombre)