from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import ProgramaEducativoForm
from django.template import loader
from django.urls import reverse
from .models import ProgramaEducativo

def RegistrarProgramaEducativo(request):
    if request.method == 'POST':

        form = ProgramaEducativoForm(request.POST)

        if form.is_valid():
            pass
    else:

        ctx = {'form': ProgramaEducativoForm()}
        return render(request, 'programaeducativo/RegistrarProgramaEducativo.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodosProgramasEducativos(request):
    programas_educativos = ProgramaEducativo.objects.all()
    lista = []
    for index, programa_educativo in enumerate(programas_educativos):
        lista.append(
            {
                0: str(index + 1),
                1: programa_educativo.get_nombre_programa_educativo,

            }
        )
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre',
        ]
    }
    context = {
        'lista': lista_data,
    }
    template = loader.get_template('programaeducativo/MostrarTodosProgramasEducativos.html')
    return HttpResponse(template.render(context, request))
