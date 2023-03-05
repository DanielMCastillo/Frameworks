from django.shortcuts import render

def hola(request):
    return render(request, 'app2/hola.html')

def mensaje(request):
    return render(request, 'app2/mensaje.html')