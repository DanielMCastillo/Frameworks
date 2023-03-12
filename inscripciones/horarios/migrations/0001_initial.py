# Generated by Django 4.1.6 on 2023-03-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('claveHorario', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('docente', models.CharField(max_length=200, verbose_name='Docente')),
                ('semestre', models.CharField(choices=[('1', '1er'), ('2', '2do'), ('3', '3er'), ('4', '4to'), ('5', '5to'), ('6', '6to'), ('7', '7mo'), ('8', '8vo'), ('9', '9no'), ('10', '10mo')], max_length=2, verbose_name='Semestre')),
                ('dia', models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado')], max_length=2, verbose_name='Dia')),
                ('hora', models.CharField(max_length=200, verbose_name='Hora')),
                ('salon', models.CharField(max_length=200, verbose_name='Salon')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materias.materia', verbose_name='Materia')),
            ],
        ),
    ]