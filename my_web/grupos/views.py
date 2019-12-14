from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import GrupoForm
from django.template import loader
from django.urls import reverse
from .models import Grupo
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def RegistrarGrupo(request):
    if request.method == 'POST':

        form = GrupoForm(request.POST)

        if form.is_valid():
            if Grupo.objects.filter(nombre=form.cleaned_data['nombre']):
                messages.error(request, 'El Grupo {} ya esta registrado'.format(form.cleaned_data['area']))
                return HttpResponseRedirect(reverse('RegistrarGrupoNuevo'))
            else:
                form.save()
                messages.success(request, 'Se ha registrado exitosamente el Grupo {}'.format((
                    form.cleaned_data['nombre']
                )))
                return HttpResponseRedirect(reverse('ObtenerTodosGrupos'))
    else:

        ctx = {'form': GrupoForm()}
        return render(request, 'grupos/RegistrarGrupo.html', ctx)

def grupo_detalle(request, grupo_id=None):
    if grupo_id is not None:
        grupo = get_object_or_404(Grupo, pk=grupo_id)
        if request.method == 'POST':
            form = GrupoForm(request.POST, instance=grupo)
            if form.is_valid():
                if Grupo.objects.filter(nombre=form.cleaned_data['nombre']):
                    messages.info(request, 'El Grupo  {} ya esta registrado'.format(form.cleaned_data['nombre']))
                    return HttpResponseRedirect(reverse('DetalleGrupo', kwargs={
                        'grupo_id': grupo_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodosGrupos'))

        else:
            form = GrupoForm(instance=grupo)
        ctx = {
            'form': form
        }
        template = loader.get_template('grupos/GrupoDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el Grupo seleccionado")



"""
Obtener todas los Grupos
"""
def ObtenerTodosGrupos(request):
    query = request.GET.get('buscar')
    if query:
        #se procede a establecer los choices
        if query == 'Alta' or query == 'alta':
            query = '1'
        if query == 'Baja' or query == 'baja':
            query = '2'
        if query == 'Suspendido' or query == 'suspendido':
            query = '3'
        grupos = Grupo.objects.filter(Q(nombre__icontains=query) | Q(estatus__icontains=query)|
                                      Q(materia__nombre__icontains=query) | Q(maestroAsignado__nombre__icontains=query))
        if not grupos:
            messages.info(request, 'No Se encontro el Grupo {}'.format(query))
    else:
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
                5: grupo.get_maestro_asignado,
                'link': {
                    'url': reverse('DetalleGrupo', kwargs={
                        'grupo_id':grupo.id
                    }),
                    'label': 'Detalle'
                },

            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    grupos_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre Grupo', 'Número de Alumnos', 'Estatus', 'Materia', 'Maestro Asignado', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': grupos_per_page

    }
    template = loader.get_template('grupos/MostrarTodosGrupos.html')
    return HttpResponse(template.render(context, request))
