from django.db import models

# Create your models here.

SEMESTRE = [
    ('1', '1er semestre'),
    ('2', '2do semestre'),
    ('3', '3er semestre'),
    ('4', '4to semestre'),
    ('5', '5to semestre'),
    ('6', '6to semestre'),
    ('7', '7mo semestre'),
    ('8', '8vo semestre'),
    ('9', '9no semestre'),
]



class Materia(models.Model):
    clave = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    creditos = models.SmallIntegerField('Creditos')
    semestre = models.CharField(max_length=2, choices=SEMESTRE)
    optativa = models.BooleanField(default=False)
    
    def __str__(self):
        return f"(self.nombre)-(self.clave)" 
        
class MateriasPrecendentes(models.Model):
    materia = models.ForeignKey("materias.Materia", verbose_name = "Materia", on_delete = models.CASCADE, related_name = "materia_actual")
    materia_precedente = models.ForeignKey("materias.Materia", verbose_name = "Materia", on_delete = models.CASCADE, related_name= 'materia_precedente')
    
    def __str__(self):
        return f"(self.materia)-(self.materia_precedente)" 
    