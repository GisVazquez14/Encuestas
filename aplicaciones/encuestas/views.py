from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, View, ListView
from aplicaciones.encuestas.models import Preguntas, Eleccion
from django.urls import reverse_lazy
from aplicaciones.encuestas.forms import PreguntaForm 
from aplicaciones.encuestas.forms import EleccionForm

class index(TemplateView):
    template_name = "encuesta/home.html"
 
class PreguntaList(ListView):
    model = Preguntas
    template_name = 'encuesta/preguntas_list.html'

class PreguntaCreate(CreateView):
    model = Preguntas
    form_class = PreguntaForm
    template_name = 'encuesta/pregunta_crear.html'
    success_url = reverse_lazy('encuestas:pregunta_list')

class EditarPregunta(UpdateView):
    model = Preguntas
    form_class = PreguntaForm
    template_name = 'encuesta/pregunta_crear.html'
    success_url = reverse_lazy('encuestas:pregunta_list')

class EliminarPregunta(DeleteView):
    model = Preguntas
    template_name = 'encuesta/eliminar.html'
    success_url = reverse_lazy('encuestas:pregunta_list')

class ListaEleccion(ListView):
    context_object_name = 'query_eleccion'
    model = Eleccion
    template_name = 'encuesta/eleccion_listar.html'
    def get_queryset(self):
        queryset = super(ListaEleccion, self).get_queryset()
        queryset = queryset.filter(user_creo=self.request.user)
        return queryset   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msn_saludo'] = 'Hola Como Estas '+str(self.request.user)
        
        return context
    

class EleccionCrear(CreateView):
    model = Eleccion
    form_class = EleccionForm
    template_name = 'encuesta/eleccion_crea.html'
    success_url = reverse_lazy('encuestas:eleccion_list')
    def form_valid(self, form):
        self.object = form.save()
        form.instance.user_creo=self.request.user
        return super().form_valid(form)

class DeleteEleccion(DeleteView):
    model = Eleccion
    template_name = 'encuesta/delete.html'
    success_url = reverse_lazy('encuestas:eleccion_list')

class EleccionUpdate(UpdateView):
    model = Eleccion
    form_class = EleccionForm
    template_name = 'encuesta/eleccion_crea.html'
    success_url = reverse_lazy('encuestas:eleccion_list')

    



    