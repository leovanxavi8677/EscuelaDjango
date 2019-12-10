from django.db import models
from django.core.validators import validate_integer
from django.core.validators import RegexValidator

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
    ('8','Post-Doctorado')
]

NIVEL_ACCESO_CHOICES = [
    ('E', 'Estudiante'),
    ('C', 'Catedratico'),
    ('A', 'Administrativo')
]




class Persona(models.Model):
    """
       validar letras
       """

    alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Solo se permiten letras y espacios', 'nombre invalido')


    """
    atributos de la persona
    """
    nombre = models.CharField(max_length=60, null=False, blank=False, validators=[alphaSpaces])
    apellidoPaterno = models.CharField(max_length=50, null=False, blank=False)
    apellidoMaterno = models.CharField(max_length=50, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    edad = models.IntegerField(blank=False, validators=[validate_integer])
    nivelEstudios = models.CharField(max_length=1, null=False, blank=False, choices=ESTUDIOS_CHOICES)
    genero = models.CharField(max_length=1, null=False, blank=False, choices=GENERO_CHOICES)
    nivelAcceso = models.CharField(max_length=1, null=False, blank=False, choices=NIVEL_ACCESO_CHOICES)
    passwd = models.CharField(max_length=150, blank=False, null=False)




    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellidoPaterno,self.apellidoMaterno)

    @property
    def get_nombre_completo(self):
        return "{} {} {}".format(
            self.nombre,
            self.apellidoPaterno,
            self.apellidoMaterno
        )

    @property
    def get_fecha_nacimiento(self):
        return "{}".format(self.fechaNacimiento)

    @property
    def get_edad(self):
        return "{}".format(self.edad)

    @property
    def get_nivel_estudios(self):
        if self.nivelEstudios == '1':
            return "Primaria"
        if self.nivelEstudios == '2':
            return "Secundaria"
        if self.nivelEstudios == '3':
            return "Bachillerato"
        if self.nivelEstudios == '4':
            return "Licenciatura"
        if self.nivelEstudios == '5':
            return "Especialidad"
        if self.nivelEstudios == '6':
            return "Maestria"
        if self.nivelEstudios == '7':
            return "Doctorado"
        if self.nivelEstudios == '8':
            return "Post-Doctorado"

    @property
    def get_genero(self):
        if self.genero == 'M':
            return "Masculino"
        else:
            return "Femenino"

    @property
    def get_nivel_acceso(self):
        if self.nivelAcceso == 'E':
            return "Estudiante"
        if self.nivelAcceso == 'C':
            return "Catedratico"
        if self.nivelAcceso == 'A':
            return "Administrativo"
    @property
    def get_password(self):
        return "{}".format(self.passwd)

    @property
    def get_nivel_acceso_caracter(self):
        return "{}".format(self.nivelAcceso)