# Generated by Django 4.1.6 on 2023-03-12 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidades_academicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramaAcademico',
            fields=[
                ('clave', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('unidad_academica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unidades_academicas.unidadacademica', verbose_name='Unidad Académica')),
            ],
        ),
    ]
