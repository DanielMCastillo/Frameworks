from django.shortcuts import render, redirect
from unidades_academicas.models import UnidadAcademica
from unidades_academicas.forms import FormUnidadAcademica


def lista_unidades(request):
    context = {
        'unidades' : UnidadAcademica.objects.all()
    }
    return render(request, 'lista_unidades.html', context)

def eliminar_unidad(request, clave):
    UnidadAcademica.objects.get(clave=clave).delete()
    return redirect('lista_unidades')
    

def nueva_unidad(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidadAcademica()
            
    context = {
        'form' : form
    }   
    return render(request, 'nueva_unidad.html', context)


def editar_unidad(request, clave):
    programa = UnidadAcademica.objects.get(clave=clave)
    
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidadAcademica(instance=programa)
            
    context = {
        'form' : form
    }   
    return render(request, 'editar_unidad.html', context)
   