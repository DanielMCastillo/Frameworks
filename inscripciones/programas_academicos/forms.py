from django import forms
from programas_academicos.models import ProgramaAcademico

class FormProgramaAcademico(forms.ModelForm):
    
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
        # fields = ['clave, nombre']