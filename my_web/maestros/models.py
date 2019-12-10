from ..personas.models import Persona
from django.db import models
from ..areamaestro.models import AreaMaestro

ESTATUS_CHOICES = [
    ('A', 'Activo'),
    ('ST', 'Suspendido'),
    ('P', 'Permiso'),
    ('SD', 'Suspendido Definitivo')
]

class Maestro(Persona):
    cubiculo = models.CharField(max_length=50, blank=False, null=False)
    numeroTrabajador = models.CharField(max_length=13, blank=False, null=False)
    estatus = models.CharField(max_length=2, blank=False, null=False, choices=ESTATUS_CHOICES)
    areamaestro = models.ForeignKey(AreaMaestro, help_text="Seleccione un Área",related_name="maestroAreaExpertise", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{}  ".format(self.get_nombre_completo)

    @property
    def get_cubiculo(self):
        return '{}'.format(self.cubiculo)

    @property
    def get_numeroTrabajador(self):
        return '{}'.format(self.numeroTrabajador)

    @property
    def get_estatus_maestro(self):
        if self.estatus == 'A':
            return 'Activo'
        if self.estatus == 'ST':
            return 'Suspendido'
        if self.estatus == 'P':
            return 'Permiso'
        if self.estatus == 'SD':
            return 'Suspendido Definitivo'

    @property
    def get_area_maestro(self):
        return '{}'.format(self.areamaestro)