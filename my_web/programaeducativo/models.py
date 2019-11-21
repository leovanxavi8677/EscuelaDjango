from django.db import models



class ProgramaEducativo(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
   
    

    def __str__(self):
        return "{}".format(self.nombre)
