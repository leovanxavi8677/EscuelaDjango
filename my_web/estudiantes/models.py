from django.db import models
from ..personas.models import Persona
from ..programaeducativo.models import ProgramaEducativo

SEMESTRE_CHOICES= [
    ('1','1er Semestre'),
    ('2','2do Semestre'),
    ('3','3er Semestre'),
    ('4','4to Semestre'),
    ('5','5nto Semestre'),
    ('6','6to Semestre'),
    ('7','7to Semestre'),
    ('8','8avo Semestre'),
    ('9','9no Semestre'),
    ('10','10mo Semestre')
]


class Estudiante(Persona):
    matricula = models.CharField(max_length=13, null=False, blank=False)
    semestre = models.CharField(max_length=2, null=False, blank=False, choices=SEMESTRE_CHOICES)
    numeroMateriasCursando= models.CharField(max_length=2,  null=False, blank=False)
    #tengo duda sobre como poner un default
    totalNumeroMateriasAprobadas= models.CharField(max_length=2, null=False, blank=False, default=0)
    #tengo duda sobre como poner un default
    totalNumerosMateriasReprobadas= models.CharField(max_length=2, default=0)
    programaEducativo= models.ForeignKey(ProgramaEducativo,help_text="Seleccione un Programa Educativo",related_name="estudianteProgramaEducativo",on_delete=models.CASCADE,null=True)
    
    

    def __str__(self):

        return "{} {} {}".format(self.nombre, self.semestre,self.numeroMateriasCursando)
