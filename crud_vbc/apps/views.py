# Create your views here.

from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

#se usará en urls.py, retorna la vista index.html
def inicio(request):
    personas = Persona.objects.all() #es un select all del modelo Persona, depende de lo q se retorne ahí traerá acá.
    contexto = {
        'personas':personas
    }
    return render(request,'index.html', contexto)


#función crear persona, usa get para cargar el formulario, y post para enviarlo
def crearPersona(request):
    if request.method == 'GET': #si es por get, mostrar formulario
        form = PersonaForm()
        contexto = {
        'form':form
    }
    else:
        form = PersonaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)


#edita por id,se obtiene la persona, si existe ese id, se llena el form, si no, se envían los datos y se edita.
def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)


def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')