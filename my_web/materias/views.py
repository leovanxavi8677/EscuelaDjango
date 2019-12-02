from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import MateriaForm
from django.template import loader
from django.urls import reverse
from .models import Materia

def RegistrarMateria(request):
    if request.method == 'POST':

        form = MateriaForm(request.POST)

        if form.is_valid():
            pass
    else:

        ctx = {'form': MateriaForm()}
        return render(request, 'materias/RegistrarMateria.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodasMaterias(request):
    materias = Materia.objects.all()
    lista = []
    for index, materia in enumerate(materias):
        lista.append(
            {
                0: str(index + 1),
                1: materia.get_nombre_materia,
                2: materia.get_estatus_materia,
                3: materia.get_area_estudio

            }
        )
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre Materia', 'Estatus', 'Área Estudio'
        ]
    }
    context = {
        'lista': lista_data,
    }
    template = loader.get_template('materias/MostrarTodasMaterias.html')
    return HttpResponse(template.render(context, request))
