from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import ProgramaEducativoForm
from django.template import loader
from django.urls import reverse
from .models import ProgramaEducativo
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def RegistrarProgramaEducativo(request):
    if request.method == 'POST':

        form = ProgramaEducativoForm(request.POST)

        if form.is_valid():
            if ProgramaEducativo.objects.filter(nombre=form.cleaned_data['nombre']):
                messages.error(request, 'El programa Educativo {} ya esta registrado'.format(
                    form.cleaned_data['nombre']
                ))
                return HttpResponseRedirect(reverse('RegistrarProgramaEducativo'))
            else:
                form.save()
                messages.success(request, 'Se ha registrado exitosamente el Programa Educativo {}'.format(
                    form.cleaned_data['nombre']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodosProgramasEducativos'))
    else:

        ctx = {'form': ProgramaEducativoForm()}
        return render(request, 'programaeducativo/RegistrarProgramaEducativo.html', ctx)

def programa_educativo_detalle(request, programaeducativo_id=None):
    if programaeducativo_id is not None:
        programa_educativo = get_object_or_404(ProgramaEducativo, pk=programaeducativo_id)
        if request.method == 'POST':
            form = ProgramaEducativoForm(request.POST, instance=programa_educativo)
            if form.is_valid():
                if ProgramaEducativo.objects.filter(nombre=form.cleaned_data['nombre']):
                    messages.info(request, 'El Programa Educativo  {} ya esta registrado'.
                                  format(form.cleaned_data['nombre']))
                    return HttpResponseRedirect(reverse('DetalleProgramaEducativo', kwargs={
                        'programaeducativo_id': programaeducativo_id
                    }))
                else:
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodosProgramasEducativos'))

        else:
            form = ProgramaEducativoForm(instance=programa_educativo)
        ctx = {
            'form': form
        }
        template = loader.get_template('programaeducativo/ProgramaEducativoDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el Programa Educativo seleccionado")


"""
Obtener todas los programas educativos
"""
def ObtenerTodosProgramasEducativos(request):
    query = request.GET.get('buscar')
    if query:
        programas_educativos = ProgramaEducativo.objects.filter(Q(nombre__icontains=query))
        if not programas_educativos:
            messages.info(request, 'No Se encontro el Programa Educativo {}'.format(query))
    else:
        programas_educativos = ProgramaEducativo.objects.all()
    lista = []
    for index, programa_educativo in enumerate(programas_educativos):
        lista.append(
            {
                0: str(index + 1),
                1: programa_educativo.get_nombre_programa_educativo,
                'link': {
                    'url': reverse('DetalleProgramaEducativo', kwargs={
                        'programaeducativo_id': programa_educativo.id
                    }),
                    'label': 'Detalle'
                },

            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    programas_educativos_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas':[
            'Id', 'Nombre', 'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': programas_educativos_per_page
    }
    template = loader.get_template('programaeducativo/MostrarTodosProgramasEducativos.html')
    return HttpResponse(template.render(context, request))
