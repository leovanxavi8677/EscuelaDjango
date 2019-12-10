from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import MaestroForm
from django.template import loader
from django.urls import reverse
from .models import Maestro
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def RegistrarMaestro(request):
    if request.method == 'POST':

        form = MaestroForm(request.POST)

        if form.is_valid():
            if Maestro.objects.filter(numeroTrabajador=form.cleaned_data['numeroTrabajador']):
                messages.error(request, 'El Número de Trabajador {} ya ha sido asignada Maestro {} {} {}'.format(
                    form.cleaned_data['numeroTrabajador'],
                    form.cleaned_data['nombre'],
                    form.cleaned_data['apellidoPaterno'],
                    form.cleaned_data['apellidoMaterno']
                ))
                return HttpResponseRedirect(reverse('RegistrarMaestroNuevo'))
            else:
                post = form.save(commit=False)
                post.nivelAcceso = 'C'
                post.save()
                messages.success(request, "Se ha registrado exitosamente el Maestr@ con Número de Trabajador {} ".format(
                    form.cleaned_data['numeroTrabajador']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodosMaestros'))

    else:

        ctx = {'form': MaestroForm()}
        return render(request, 'maestros/RegistrarMaestro.html', ctx)


def maestro_detalle(request, maestro_id=None):
    if maestro_id is not None:
        maestro = get_object_or_404(Maestro, pk=maestro_id)
        if request.method == 'POST':
            form = MaestroForm(request.POST, instance=maestro)
            if form.is_valid():
                if Maestro.objects.filter(numeroTrabajador=form.cleaned_data['numeroTrabajador']):
                    messages.info(request, 'El Número de Trabajador {} ya esta registrada'.
                                  format(form.cleaned_data['numeroTrabajador']))
                    return HttpResponseRedirect(reverse('DetalleMaestro', kwargs={
                        'maestro_id': maestro_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodosMaestros'))

        else:
            form = MaestroForm(instance=maestro)
        ctx = {
            'form': form
        }
        template = loader.get_template('maestros/MaestroDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el Maestro  seleccionad@")


"""
Obtener todos los Maestros
"""
def ObtenerTodosMaestros(request):
    query = request.GET.get('buscar')
    if query:
        # se procede a establecer los choices del estatus del maestro en caso de que el query lo tenga
        if query == 'Activo' or query == 'activo':
            query = 'A'
        if query == 'Suspendido' or query == 'suspendido':
            query = 'ST'
        if query == 'Permiso' or query == 'permiso':
            query = 'P'
        if query == 'Suspendido Definitivo' or query == 'suspendido definitivo':
            query = 'SD'
        maestros = Maestro.objects.filter(Q(nombre__icontains=query) | Q(estatus__icontains=query) |
                                          Q(numeroTrabajador__icontains=query)
                                          | Q(apellidoPaterno__icontains=query) | Q(apellidoMaterno__icontains=query ))
    else:
        maestros = Maestro.objects.all()
    lista = []
    for index, maestro in enumerate(maestros):
        lista.append(
            {
                0: str(index),
                1: maestro.get_nombre_completo,
                2: maestro.get_fecha_nacimiento,
                3: maestro.get_edad,
                4: maestro.get_nivel_estudios,
                5: maestro.get_genero,
                6: maestro.get_nivel_acceso,
                7: maestro.get_cubiculo,
                8: maestro.get_numeroTrabajador,
                9: maestro.get_estatus_maestro,
                10: maestro.get_area_maestro,
                'link': {
                    'url': reverse('DetalleMaestro', kwargs={
                        'maestro_id': maestro.id
                    }),
                    'label': 'Detalle'
                },


            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    maestros_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre', 'Fecha Nacimiento', 'Edad', 'Nivel Estudios', 'Genero', 'Nivel Acceso', 'Cubiculos',
            'Número de Trabajador', 'Estatus', 'Área Maestro', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': maestros_per_page
    }
    template = loader.get_template('maestros/MostrarTodosMaestros.html')
    return HttpResponse(template.render(context, request))