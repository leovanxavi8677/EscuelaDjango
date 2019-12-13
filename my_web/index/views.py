from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from .forms import IndexForm
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from ..estudiantes.models import Estudiante
from ..maestros.models import Maestro


def iniciar_sesion(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            usuario = str(form.cleaned_data['usuario']).strip()
            password = str(form.cleaned_data['password']).strip()
            if usuario and password:  # si usuario y password no estan vacios

                if usuario[0] == '1':  # si el primer carácter es 1 es un estudiante el que esta ingresando
                    try:
                        estudiante = Estudiante.objects.get(matricula=usuario)
                    except Estudiante.DoesNotExist:
                        context ={
                            'username': usuario
                        }
                        #return render_to_response('index/error_inicio_session.html')
                        template = loader.get_template('index/error_inicio_session.html')
                        return HttpResponse(template.render(context, request))
                    messages.info(request, 'entro estudiante')
                    if estudiante:
                        if estudiante.get_password == password:
                            request.session['nivel_acceso'] = estudiante.get_nivel_acceso_caracter
                            context = {
                                'nombre_completo': estudiante.get_nombre_completo,
                            }
                            template = loader.get_template('index/PaginaPrincipal.html')
                            return HttpResponse(template.render(context, request))
                        else:
                            messages.error(request, 'La contraseña no es la correcta')
                            return HttpResponseRedirect(reverse('iniciosesion'))

                if usuario[0] == '2':  # si el primer carácter es 2 es una maestro el que esta accediendo
                    try:
                        maestro = Maestro.objects.get(numeroTrabajador=usuario)
                    except Maestro.DoesNotExist:
                        context = {
                            'username': usuario
                        }
                        template = loader.get_template('index/error_inicio_session.html')
                        return HttpResponse(template.render(context, request))
                    messages.info(request, 'entro maestro')
                    if maestro:
                        if maestro.get_password == password:
                            request.session['nivel_acceso'] = maestro.get_nivel_acceso_caracter
                            context = {
                                'nombre_completo': maestro.get_nombre_completo,
                            }
                            template = loader.get_template('index/PaginaPrincipal.html')
                            return HttpResponse(template.render(context, request))
                        else:
                            messages.error(request, 'La contraseña no es la correcta')
                            return HttpResponseRedirect(reverse('iniciosesion'))

                if usuario[0] == '3':  # si el primer carácter es 3 es es un administrativo el que esta accediendo
                    pass

    else:

        ctx = {'form': IndexForm()}
        return render(request, 'index/index.html', ctx)


def mostrar_pagina_principal(request):
    return render(request, 'index/PaginaPrincipal.html')
