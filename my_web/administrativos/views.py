from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import AdministrativoForm
from django.template import loader
from django.urls import reverse
from .models import Administrativo
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def RegistrarAdministrativo(request):
    if request.method == 'POST':

        form = AdministrativoForm(request.POST)

        if form.is_valid():
            if Administrativo.objects.filter(numeroAdministrativo=form.cleaned_data['numeroAdministrativo']):
                messages.error(request, 'El numeroAdministrativo {} ya ha sido asignado'.format(
                    form.cleaned_data['numeroAdministrativo'],
                ))
                return HttpResponseRedirect(reverse('RegistrarAdministrativoNuevo'))
            else:
                post = form.save(commit=False)
                post.nivelAcceso = 'A'
                post.save()
                messages.success(request, "Se ha registrado exitosamente el Administrativo con numeroAdministrativo {} ".format(
                    form.cleaned_data['numeroAdministrativo']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodosAdministrativos'))

    else:

        ctx = {'form': AdministrativoForm()}
        return render(request, 'administrativos/RegistrarAdministrativo.html', ctx)

def administrativo_detalle(request, administrativo_id=None):
    if administrativo_id is not None:
        administrativo = get_object_or_404(Administrativo, pk=administrativo_id)
        if request.method == 'POST':
            form = AdministrativoForm(request.POST, instance=administrativo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se ha actualizado el registro')
                return HttpResponseRedirect(reverse('ObtenerTodosAdministrativos'))
        else:
            form = AdministrativoForm(instance=administrativo)
        ctx = {
            'form': form
        }
        template = loader.get_template('administrativos/AdministrativoDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el Administrativo  seleccionad@")

"""
Obtener todos los administrativos
"""
def ObtenerTodosAdministrativos(request):
    query = request.GET.get('buscar')
    if query:
        administrativos = Administrativo.objects.filter(Q(nombre__icontains=query) | Q(numeroAdministrativo__icontains=query)
                                                | Q(apellidoPaterno__icontains=query) | Q(apellidoMaterno__icontains=query ))
        if not administrativos:
            messages.info(request, 'No Se encontro el Administrativo {}'.format(query))
    else:
        administrativos = Administrativo.objects.all()
    lista = []
    for index, administrativo in enumerate(administrativos):
        lista.append(
            {
                0: str(index + 1),
                1: administrativo.get_nombre_completo,
                2: administrativo.get_fecha_nacimiento,
                3: administrativo.get_edad,
                4: administrativo.get_nivel_estudios,
                5: administrativo.get_genero,
                6: administrativo.get_nivel_acceso,
                7: administrativo.get_numero_administrativo,
                8: administrativo.get_numero_oficina,
                'link': {
                    'url': reverse('DetalleAdministrativo', kwargs={
                        'administrativo_id': administrativo.id
                    }),
                    'label': 'Detalle'
                },


            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    administrativos_per_page = paginator.get_page(page)
    lista_data = {
        'lista': lista,
        'columnas': [
            'Id',
            'Nombre',
            'Fecha Nacimiento',
            'Edad',
            'Nivel Estudios',
            'Genero',
            'Nivel Acceso',
            'Número Administrativo',
            'Número de Oficina',
            'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': administrativos_per_page
    }
    template = loader.get_template('administrativos/MostrarTodosAdministrativos.html')
    return HttpResponse(template.render(context, request))
