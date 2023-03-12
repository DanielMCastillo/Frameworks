from django import forms

from materias.models import Materia
from .models import Horario

class FormHorario(forms.ModelForm):
    
    class Meta:
        model = Horario
        fields = '__all__'
        # fields = ['clave, nombre']

class FormHorarioEditar(FormHorario):
    class Meta:
        exclude = ['clave']
        model = Horario
        
