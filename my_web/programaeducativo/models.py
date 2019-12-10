from django.db import models
from django.core.validators import validate_slug


class ProgramaEducativo(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False, validators=[validate_slug])
   
    

    def __str__(self):
        return "{}".format(self.nombre)

    @property
    def get_nombre_programa_educativo(self):
        return "{}".format(self.nombre)
