
from django.db import models


class AreaMaestro(models.Model):
    area = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return "{}".format(self.area)

    @property
    def get_area(self):
        return "{}".format(self.area)