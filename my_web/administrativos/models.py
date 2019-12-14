from django.db import models
from ..personas.models import Persona
from django.core.validators import validate_integer, validate_slug

class Administrativo(Persona):
    numeroAdministrativo = models.CharField(max_length=13, blank=False, null=False, validators=[validate_slug])
    numeroOficina = models.CharField(max_length=3, blank=False, null=False, validators=[validate_integer])

    def __str__(self):
        return "{} {}".format(
            self.get_nombre_completo,
            self.get_numero_administrativo
        )

    @property
    def get_numero_administrativo(self):
        return "{}".format(
            self.numeroAdministrativo
        )

    @property
    def get_numero_oficina(self):
        return "{}".format(
            self.numeroOficina
        )
