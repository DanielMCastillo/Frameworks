from django.shortcuts import render
from django.views.generic import ListView
from .models import Materia

# Create your views here.
class ListaMaterias(ListView):
    model = Materia

