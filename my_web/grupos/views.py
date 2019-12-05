from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import GrupoForm
from django.template import loader
from django.urls import reverse
from .models import Grupo

def RegistrarGrupo(request):
    if request.method == 'POST':

        form = GrupoForm(request.POST)

        if form.is_valid():
            pass
    else:

        ctx = {'form': GrupoForm()}
        return render(request, 'grupos/RegistrarGrupo.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodosGrupos(request):
    grupos = Grupo.objects.all()
    lista = []
    for index, grupo in enumerate(grupos):
        lista.append(
            {
                0: str(index + 1),
                1: grupo.get_nombre_grupo,
                2: grupo.get_numero_alumnos,
                3: grupo.get_estatus,
                4: grupo.get_materia_grupo,
                5: grupo.get_maestro_asignado

            }
        )
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre Grupo', 'Número de Alumnos', 'Estatus', 'Materia', 'Maestro Asignado'
        ]
    }
    context = {
        'lista': lista_data,

    }
    template = loader.get_template('grupos/MostrarTodosGrupos.html')
    return HttpResponse(template.render(context, request))
