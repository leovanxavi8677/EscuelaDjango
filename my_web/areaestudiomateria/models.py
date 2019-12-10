from django.db import models
from django.core.validators import validate_slug


class AreaEstudioMateria(models.Model):
    area = models.CharField(max_length=50, blank=False, null=False, validators=[validate_slug])


    def __str__(self):
        return "{}".format(self.area)

    @property
    def get_area(self):
        return "{}".format(self.area)


