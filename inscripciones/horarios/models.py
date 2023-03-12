from django.db import models

SEMESTRES = [
    ('1', '1er'),
    ('2', '2do'),
    ('3', '3er'),
    ('4', '4to'),
    ('5', '5to'),
    ('6', '6to'),
    ('7', '7mo'),
    ('8', '8vo'),
    ('9', '9no'),
    ('10', '10mo'),
]

DIAS = [
    ('1', 'Lunes'),
    ('2', 'Martes'),
    ('3', 'Miercoles'),
    ('4', 'Jueves'),
    ('5', 'Viernes'),
    ('6', 'Sabado'),
]


class Horario(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    materia = models.ForeignKey("materias.Materia", verbose_name='Materia', on_delete=models.DO_NOTHING)
    docente = models.CharField('Docente', max_length=200)
    semestre = models.CharField('Semestre' , max_length=2, choices=SEMESTRES)
    dia = models.CharField('Dia' , max_length=2, choices=DIAS)
    hora = models.CharField('Hora', max_length=200)
    salon = models.CharField('Salon', max_length=200)

    def __str__(self):
        return self.materia 
    
