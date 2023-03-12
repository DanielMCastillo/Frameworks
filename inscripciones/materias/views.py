from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Materia
from .forms import FormMateria, FormMateriaEditar, FiltrosMateria


class Bienvenida(TemplateView):
    template_name = 'home.html'

class ListaMaterias(ListView):
    model = Materia
    extra_context = {'form': FiltrosMateria}

    
class NuevaMateria(CreateView):
    model = Materia
    form_class = FormMateria
    # fields = '__all__'
    success_url = reverse_lazy('lista_materias')
    extra_context = {'accion': 'Nueva'}
    
    # template_name = 'alta_materia.html'
    # fields = ['nombre','clave','semestre']
    
class EditarMateria(UpdateView):
    model = Materia
    form_class = FormMateriaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_materias')
    
class EliminarMateria(DeleteView):
    model = Materia
    success_url = reverse_lazy('lista_materias')
    
def buscar_materia(request):
    materias = Materia.objects.all()
    
    if request.method == 'POST':
        form = FiltrosMateria(request.POST)
        print(request.POST)
        clave = request.POST.get('clave',None)
        nombre = request.POST.get('nombre',None)
        semestre = request.POST.get('semestre',None)
        creditos = request.POST.get('creditos',None)
        optativa = request.POST.get('optativa',None)
        if clave:
            materias = materias.filter(clave=clave)
        if nombre:
            materias = materias.filter(nombre=nombre)
        if semestre:
            materias = materias.filter(semestre=semestre)
        if creditos:
            materias = materias.filter(creditos=creditos)
        if optativa:
            materias = materias.filter(optativa=optativa)
            
        
    else:
        form = FiltrosMateria()      
    context = {
        'object_list': materias,
        'form': form
    } 
    return render(request, 'materias/materia_list.html', context)
        
