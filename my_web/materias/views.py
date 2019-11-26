from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import MateriaForm

def index(request):
    if request.method == 'POST':

        #se crea una instancia de una forma y se llena con los datos creados del request
        form = MateriaForm(request.POST)
        #checa si es valida
        if form.is_valid():
            #return HttpResponseRedirect('/thanks/')


    else:#si es GET se creara en blanco el formulario
        form = MateriaForm()

    return render(request, 'RegistrarMateria.html', {
        'form': form,
    })

def gracias(reques):
    html = '<html><body>"Datos enviados" </body><html>'
    return HttpResponse(html)
