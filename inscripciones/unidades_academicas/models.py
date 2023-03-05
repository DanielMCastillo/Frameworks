from django.db import models


class UnidadAcademica(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    nombre = models.CharField('Nombre', max_length=200)
    direccion = models.CharField('Dirección', max_length=350, default='sin dirección')

    def __str__(self):
        return self.nombre 