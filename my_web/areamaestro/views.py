from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import AreaMaestroForm
from django.template import loader
from django.urls import reverse
from .models import AreaMaestro

def RegistrarAreaMaestro(request):
    if request.method == 'POST':

        form = AreaMaestroForm(request.POST)

        if form.is_valid():
            pass
    else:

        ctx = {'form': AreaMaestroForm()}
        return render(request, 'areamaestro/RegistrarAreaMaestro.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodosAreasMaestro(request):
    areas = AreaMaestro.objects.all()
    lista = []
    for index, area in enumerate(areas):
        lista.append(
            {
                0: str(index + 1),
                1: area.get_area

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
    template = loader.get_template('areamaestro/MostrarTodasAreasMaestro.html')
    return HttpResponse(template.render(context, request))
