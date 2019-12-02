from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import AreaEstudioMateriaForm
from django.template import loader
from django.urls import reverse
from .models import AreaEstudioMateria

def RegistrarAreaEstudioMateria(request):
    if request.method == 'POST':

        form = AreaEstudioMateriaForm(request.POST)

        if form.is_valid():
            form.save()
            reverse("ListingAreasEstudioMaterias")
    else:

        ctx = {'form': AreaEstudioMateriaForm()}
        return render(request, 'areaestudiomateria/RegistrarAreaEstudioMateria.html', ctx)

"""
Obtener todas las materias
"""
def ObtenerTodosAreasEstudioMateria(request):
    areas = AreaEstudioMateria.objects.all()
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
    template = loader.get_template('areaestudiomateria/MostrarTodasAreasEstudioMaterias.html')
    return HttpResponse(template.render(context, request))
