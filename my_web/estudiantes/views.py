from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import EstudianteForm
from django.template import loader
from django.urls import reverse
from .models import Estudiante

def RegistrarEstudiante(request):
    if request.method == 'POST':

        form = EstudianteForm(request.POST)

        if form.is_valid():
            pass
    else:

        ctx = {'form': EstudianteForm()}
        return render(request, 'estudiantes/RegistrarEstudiante.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodosEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    lista = []
    for index, estudiante in enumerate(estudiantes):
        lista.append(
            {
                0: str(index + 1),
                1: estudiante.get_nombre_completo,
                2: estudiante.get_fecha_nacimiento,
                3: estudiante.get_edad,
                4: estudiante.get_nivel_estudios,
                5: estudiante.get_genero,
                6: estudiante.get_nivel_acceso,
                7: estudiante.get_matricula,
                8: estudiante.get_semestre,
                9: estudiante.get_numero_materias_cursando,
                10: estudiante.get_total_materias_aprobadas,
                11: estudiante.get_total_mateiras_reprobadas,
                12: estudiante.get_programa_educativo,
                13: estudiante.get_materias


            }
        )
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre', 'Fecha Nacimiento', 'Edad', 'Nivel Estudios', 'Genero', 'Nivel Acceso', 'Matricula',
            'Semestre', 'Número Materias Cursando', 'Total Materias Aprobadas', 'Total Materias Reprobadas',
            'Programa Educativo', 'Materias'
        ]
    }
    context = {
        'lista': lista_data,
    }
    template = loader.get_template('estudiantes/MostrarTodosEstudiantes.html')
    return HttpResponse(template.render(context, request))
