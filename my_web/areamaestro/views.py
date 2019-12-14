from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import AreaMaestroForm
from django.template import loader
from django.urls import reverse
from .models import AreaMaestro
from django.contrib import messages
from django.core.paginator import Paginator


def RegistrarAreaMaestro(request):
    if request.method == 'POST':

        form = AreaMaestroForm(request.POST)

        if form.is_valid():
            if AreaMaestro.objects.filter(area=form.cleaned_data['area']):
                messages.error(request, 'El Área {} ya esta registrada'.format(form.cleaned_data['area']))
                return HttpResponseRedirect(reverse('RegistrarAreaMaestro'))
            else:
                form.save()
                messages.success(request, 'Se ha registra exitosamente el Área de Maestro {}'.format(
                    form.cleaned_data['area']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodosAreasMaestro'))
    else:

        ctx = {'form': AreaMaestroForm()}
        return render(request, 'areamaestro/RegistrarAreaMaestro.html', ctx)


def area_maestro_detalle(request, area_id=None):
    if area_id is not None:
        area = get_object_or_404(AreaMaestro, pk=area_id)
        if request.method == 'POST':
            form = AreaMaestroForm(request.POST, instance=area)
            if form.is_valid():
                if AreaMaestro.objects.filter(area=form.cleaned_data['area']):
                    messages.info(request, 'El Área {} ya esta registrada'.format(form.cleaned_data['area']))
                    return HttpResponseRedirect(reverse('DetalleAreaMaestro', kwargs={
                        'area_id': area_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodosAreasMaestro'))

        else:
            form = AreaMaestroForm(instance=area)
        ctx = {
            'form': form
        }
        template = loader.get_template('areamaestro/AreaMaestroDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el area de estudio de seleccionada")
"""
Obtener todas las areas del maestro
"""
def ObtenerTodosAreasMaestro(request):
    query = request.GET.get('buscar')
    if query:
        query = request.GET.get('buscar')
        areas = AreaMaestro.objects.filter(area__icontains=query)
        if not areas:
            messages.info(request, 'No Se encontro el Área de Maestro {}'.format(query))
    else:
        areas = AreaMaestro.objects.all()
    lista = []
    for index, area in enumerate(areas):
        lista.append(
            {
                0: str(index + 1),
                1: area.get_area,
                'link': {
                    'url': reverse('DetalleAreaMaestro', kwargs={
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
        'columnas':[
            'Id', 'Nombre', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': areas_per_page,
    }
    template = loader.get_template('areamaestro/MostrarTodasAreasMaestro.html')
    return HttpResponse(template.render(context, request))
