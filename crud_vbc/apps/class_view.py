from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona

#Todo hereda de la clase View,
#Clase que retorna la lista de la tabla, se envía a la urls.py, en el for del index, se cambia Personas, por objeto de clase
class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

    """
    #query para filtrar los 2 últimos
    def get_queryset(self):
        return self.model.objects.all()[:2]
    """


#clase que crea persona,
class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')


#clase que updatea... dentro de la url, se cambia la id de gel por pk
class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')


class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')