from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .forms import EstudianteForm
from django.template import loader
from django.urls import reverse
from .models import Estudiante
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def RegistrarEstudiante(request):
    if request.method == 'POST':

        form = EstudianteForm(request.POST)

        if form.is_valid():
            if Estudiante.objects.filter(matricula=form.cleaned_data['matricula']):
                messages.error(request, 'La matricula {} ya ha sido asignada al estudiante {} {} {}'.format(
                    form.cleaned_data['matricula'],
                    form.cleaned_data['nombre'],
                    form.cleaned_data['apellidoPaterno'],
                    form.cleaned_data['apellidoMaterno']
                ))
                return HttpResponseRedirect(reverse('RegistrarEstudianteNuevo'))
            else:
                post = form.save(commit=False)
                post.nivelAcceso = 'E'
                post.save()
                messages.success(request, "Se ha registrado exitosamente el Esudidante con matricula {} ".format(
                    form.cleaned_data['matricula']
                ))
                return HttpResponseRedirect(reverse('ObtenerTodosEstudiantes'))

    else:

        ctx = {'form': EstudianteForm()}
        return render(request, 'estudiantes/RegistrarEstudiante.html', ctx)


def estudainte_detalle(request, estudiante_id=None):
    if estudiante_id is not None:
        estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
        if request.method == 'POST':
            form = EstudianteForm(request.POST, instance=estudiante)
            if form.is_valid():
                matricula_vieja=estudiante.get_matricula
                matricula_nueva=form.cleaned_data.get['matricula']
                messages.info(request, 'matricula vieja {} y matricula nueva {}'.format(matricula_vieja, matricula_nueva))

                if matricula_nueva == matricula_vieja: #si la matricula es la misma puede hacer los cambios
                    messages.info(request, 'no nay cambio matricula')
                    form.save()
                    messages.success(request, 'Se ha actualizado el registro')
                    return HttpResponseRedirect(reverse('ObtenerTodosEstudiantes'))
                else:#si la matricula la cambio
                    messages.info(request, 'entro en cambio')
                    if Estudiante.objects.filter(Q(matricula=form.cleaned_data['matricula'])):
                        messages.info(request, 'La matricula {} ya esta registrada'.format(form.cleaned_data['matricula']))
                        return HttpResponseRedirect(reverse('DetalleEstudiante', kwargs={
                            'estudiante_id': estudiante_id
                        }))
                    else:
                        form.save()
                        messages.success(request, 'Se ha actualizado el registro')
                        return HttpResponseRedirect(reverse('ObtenerTodosEstudiantes'))

        else:
            form = EstudianteForm(instance=estudiante)
        ctx = {
            'form': form
        }
        template = loader.get_template('estudiantes/EstudianteDetalle.html')
        return HttpResponse(template.render(ctx, request))
    raise Http404("No existe el estudiante  seleccionad@")


"""
Obtener todos los estudiantes
"""
def ObtenerTodosEstudiantes(request):
    query = request.GET.get('buscar')
    if query:
        estudiantes = Estudiante.objects.filter(Q(nombre__icontains=query) | Q(matricula__icontains=query)
                                                | Q(apellidoPaterno__icontains=query) | Q(apellidoMaterno__icontains=query ))
    else:
        estudiantes = Estudiante.objects.all()
    lista = []
    for index, estudiante in enumerate(estudiantes):
        lista.append(
            {
                0: str(index + 1),
                1: estudiante.get_nombre_completo,
                2: estudiante.get_fecha_nacimiento,
                3: estudiante.get_edad,
                4: estudiante.get_nivel_estudios,
                5: estudiante.get_genero,
                6: estudiante.get_nivel_acceso,
                7: estudiante.get_matricula,
                8: estudiante.get_semestre,
                9: estudiante.get_numero_materias_cursando,
                10: estudiante.get_total_materias_aprobadas,
                11: estudiante.get_total_mateiras_reprobadas,
                12: estudiante.get_programa_educativo,
                13: estudiante.get_materias,
                'link': {
                    'url': reverse('DetalleEstudiante', kwargs={
                        'estudiante_id': estudiante.id
                    }),
                    'label': 'Detalle'
                },


            }
        )
    paginator = Paginator(lista, 4)  # paginación
    page = request.GET.get('page')
    estudiantes_per_page = paginator.get_page(page)
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
            'Matricula',
            'Semestre',
            'Número Materias Cursando',
            'Total Materias Aprobadas',
            'Total Materias Reprobadas',
            'Programa Educativo',
            'Materias',
            'Detalle'
        ]
    }
    context = {
        'lista': lista_data,
        'items_per_page': estudiantes_per_page
    }
    template = loader.get_template('estudiantes/MostrarTodosEstudiantes.html')
    return HttpResponse(template.render(context, request))
