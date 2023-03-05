from django.shortcuts import render, redirect
from programas_academicos.models import ProgramaAcademico
from programas_academicos.forms import FormProgramaAcademico


def lista_programas(request):
    context = {
        'programas' : ProgramaAcademico.objects.all()
    }
    return render(request, 'lista_programas.html', context)

def eliminar_programa(request, clave):
    ProgramaAcademico.objects.get(clave=clave).delete()
    return redirect('lista_programas')
    

def nuevo_programa(request):
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormProgramaAcademico()
            
    context = {
        'form' : form
    }   
    return render(request, 'nuevo_programa.html', context)


def editar_programa(request, clave):
    programa = ProgramaAcademico.objects.get(clave=clave)
    
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormProgramaAcademico(instance=programa)
            
    context = {
        'form' : form
    }   
    return render(request, 'editar_programa.html', context)
   