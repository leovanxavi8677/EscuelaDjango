from django.db import models

GENERO_CHOICES = [
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
]

ESTUDIOS_CHOICES =[
    ('1','Primaria'),
    ('2','Secundaria'),
    ('3','Bachillerato'),
    ('4','Licenciatura'),
    ('5','Especialidad'),
    ('6','Maestria'),
    ('7','Doctorado'),
    ('9','Post-Doctorado')
]

NIVEL_ACCESO_CHOICES = [
    ('E','Estudiante'),
    ('C','Catedratico'),
    ('A','Administrativo')
]




class Persona(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
    apellidoPaterno = models.CharField(max_length=50, null=False, blank=False)
    apellidoMaterno = models.CharField(max_length=50, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    edad = models.IntegerField(blank=False)
    nivelEstudios = models.CharField(max_length=1, null=False, blank=False, choices=ESTUDIOS_CHOICES)
    genero = models.CharField(max_length=1, null=False, blank=False, choices=GENERO_CHOICES)
    nivelAcceso = models.CharField(max_length=1, null=False, blank=False, choices=NIVEL_ACCESO_CHOICES)
    passwd = models.CharField(max_length=150, blank=False, null=False)
    

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellidoPaterno,self.apellidoMaterno)
