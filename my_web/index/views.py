from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import IndexForm
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from ..estudiantes.models import Estudiante
from ..personas import models as persona
def iniciar_sesion(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            usuario = str(form.cleaned_data['usuario']).strip()
            password = str(form.cleaned_data['password']).strip()
            if usuario and password: # si usuario y password no estan vacios

                if usuario[0] == '1':# si el primer carácter es 1 es un estudiante el que esta ingresando

                    estudiante = Estudiante.objects.get(matricula=usuario)
                    if Estudiante:
                        if estudiante.get_password == password:
                            return HttpResponseRedirect(reverse('paginaprincipal'))
                        else:
                            messages.error(request, 'La contraseña no es la correcta')
                            return HttpResponseRedirect(reverse('iniciosesion'))
                if usuario[0] == '2': #si el primer carácter es 2 es una maestro el que esta accediendo
                    pass
                if usuario[0] == '3': #si el primer carácter es 3 es es un administrativo el que esta accediendo
                    pass

    else:

        ctx = {'form': IndexForm()}
        return render(request, 'index/index.html', ctx)

def mostrar_pagina_principal(request):
    return render(request, 'index/PaginaPrincipal.html')
