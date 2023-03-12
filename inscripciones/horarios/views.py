from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horario
from .forms import FormHorario, FormHorarioEditar


def lista_horarios(request):
    context = {
        'horarios' : Horario.objects.all()
    }
    return render(request, 'lista_horarios.html', context)

def eliminar_horario(request, clave):
    Horario.objects.get(clave=clave).delete()
    return redirect('lista_horarios')
    

def nuevo_horario(request):
    if request.method == 'POST':
        form = FormHorario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_horarios')
    else:
        form = FormHorario()
            
    context = {
        'form' : form
    }   
    return render(request, 'nuevo_horario.html', context)


def editar_horario(request, clave):
    programa = Horario.objects.get(clave=clave)
    
    if request.method == 'POST':
        form = FormHorario(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('lista_horarios')
    else:
        form = FormHorario(instance=programa)
            
    context = {
        'form' : form
    }   
    return render(request, 'editar_horario.html', context)
   