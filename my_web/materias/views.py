from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import MateriaForm
from django.template import loader
from django.urls import reverse
from .models import Materia
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def RegistrarMateria(request):
    if request.method == 'POST':

        form = MateriaForm(request.POST)

        if form.is_valid():
            if Materia.objects.filter(nombre=form.cleaned_data['nombre']):
                messages.error(request, 'La materia {} ya ha sido registrada'.format(
                    form.cleaned_data['nombre']
                ))
                return HttpResponseRedirect(reverse('RegistrarMateria'))
            else:
                form.save()
                messages.success(request, 'Se ha registrado exitosamente la materia {}'.format(
                    form.cleaned_data['nombre']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodasMaterias'))
    else:

        ctx = {'form': MateriaForm()}
        return render(request, 'materias/RegistrarMateria.html', ctx)

def materia_detalle(request, materia_id=None):
    if materia_id is not None:
        materia = get_object_or_404(Materia, pk=materia_id)
        if request.method == 'POST':
            form = MateriaForm(request.POST, instance=materia)
            if form.is_valid():
                if Materia.objects.filter(nombre=form.cleaned_data['nombre']):
                    messages.info(request, 'La materia {} ya esta registrada'.format(form.cleaned_data['nombre']))
                    return HttpResponseRedirect(reverse('DetalleMateria', kwargs={
                        'materia_id': materia_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodasMaterias'))

        else:
            form = MateriaForm(instance=materia)
        ctx = {
            'form': form
        }
        template = loader.get_template('materias/MateriaDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe la materia  seleccionada")


"""
Obtener todas las materias
"""
def ObtenerTodasMaterias(request):
    query = request.GET.get('buscar')
    if query:
        if query == 'Alta' or query == 'alta':
            query = '1'
        if query == 'Pendiente' or query == 'pendiente':
            query = '2'
        if query == 'Baja' or query == 'baja':
            query = '3'
        materias = Materia.objects.filter(Q(nombre__icontains=query) | Q(estatusMateria__icontains=query) |
                                          Q(areaEstudio__area__icontains=query))
    else:
        materias = Materia.objects.all()
    lista = []
    for index, materia in enumerate(materias):
        lista.append(
            {
                0: str(index + 1),
                1: materia.get_nombre_materia,
                2: materia.get_estatus_materia,
                3: materia.get_area_estudio,
                'link': {
                    'url': reverse('DetalleMateria', kwargs={
                        'materia_id': materia.id
                    }),
                    'label': 'Detalle'
                },

            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    materias_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre Materia', 'Estatus', 'Área Estudio', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': materias_per_page
    }
    template = loader.get_template('materias/MostrarTodasMaterias.html')
    return HttpResponse(template.render(context, request))
