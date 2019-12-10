from django.db import models
from ..areaestudiomateria.models import AreaEstudioMateria
from django.core.validators import validate_slug

ESTATUS_MATERIA=[
    ('1', 'Alta'),
    ('2', 'Pendiente'),
    ('3', 'Baja')
]



class Materia(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, validators=[validate_slug])
    estatusMateria = models.CharField(max_length=1, blank=False, null=False, choices=ESTATUS_MATERIA)
    areaEstudio = models.ForeignKey(AreaEstudioMateria, related_name="materiaAreaEstudioMateria",
                                    on_delete=models.CASCADE,null=True,
                                    help_text="Seleccione una Área de Estudio")

    def __str__(self):
        return "{}".format(self.nombre)

    @property
    def get_nombre_materia(self):
        return "{}".format(self.nombre)

    @property
    def get_estatus_materia(self):
        if self.estatusMateria == '1':
            return "Alta"
        if self.estatusMateria == '2':
            return "Pendiente"
        if self.estatusMateria == '3':
            return "Baja"

    @property
    def get_area_estudio(self):
        return "{}".format(self.areaEstudio)