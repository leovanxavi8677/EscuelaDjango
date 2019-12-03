from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AreaEstudioMateriaForm
from django.template import loader
from django.urls import reverse
from .models import AreaEstudioMateria
from django.contrib import messages
from django.core.paginator import Paginator


def RegistrarAreaEstudioMateria(request):
    if request.method == 'POST':

        form = AreaEstudioMateriaForm(request.POST)

        if form.is_valid():
            if AreaEstudioMateria.objects.filter(area=form.cleaned_data['area']):
                messages.error(request, 'El Área {} ya esta registrada'.format(form.cleaned_data['area']))
                return HttpResponseRedirect(reverse('RegistrarNuevaAreaEstudioMateria'))
            else:
                form.save()
                messages.success(request, "Se ha registrado existosamente el Área de Estudio {}".format(
                    form.cleaned_data['area']))
                return HttpResponseRedirect(reverse('ListingAreasEstudioMaterias'))

    else:

        ctx = {'form': AreaEstudioMateriaForm()}
        return render(request, 'areaestudiomateria/RegistrarAreaEstudioMateria.html', ctx)


def area_estudio__materia_detalle(request, area_id=None):
    if area_id is not None:
        area = get_object_or_404(AreaEstudioMateria, pk=area_id)
        if request.method == 'POST':
            form = AreaEstudioMateriaForm(request.POST, instance=area)
            if form.is_valid():
                if AreaEstudioMateria.objects.filter(area=form.cleaned_data['area']):
                    messages.info(request, 'El Área {} ya esta registrada'.format(form.cleaned_data['area']))
                    return HttpResponseRedirect(reverse('DetalleAreaEstudio', kwargs={
                        'area_id': area_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ListingAreasEstudioMaterias'))

        else:
            form = AreaEstudioMateriaForm(instance=area)
        ctx = {
            'form': form
        }
        template = loader.get_template('areaestudiomateria/AreaEstudioDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el area de estudio de seleccionada")


"""
Obtener todas las materias
"""


def ObtenerTodosAreasEstudioMateria(request):
    query = request.GET.get('buscar')
    if query:
        query = request.GET.get('buscar')
        areas = AreaEstudioMateria.objects.filter(area__icontains=query)
    else:
        areas = AreaEstudioMateria.objects.all()
    lista = []

    for index, area in enumerate(areas):
        lista.append(
            {
                0: str(index + 1),
                1: area.get_area,
                'link': {
                    'url': reverse('DetalleAreaEstudio', kwargs={
                        'area_id': area.id
                    }),
                    'label': 'Detalle'

                },

            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    areas_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas': [
            'Id', 'Nombre', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'areas_per_page': areas_per_page,
    }
    template = loader.get_template('areaestudiomateria/MostrarTodasAreasEstudioMaterias.html')
    return HttpResponse(template.render(context, request))
