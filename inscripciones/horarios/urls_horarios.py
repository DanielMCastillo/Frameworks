from django.urls import path, include
from horarios import views

urlpatterns = [
    path('', views.lista_horarios, name='lista_horarios'),
    path('nuevo', views.nuevo_horario, name='nuevo_horario'),
    path('eliminar/<int:clave>', views.eliminar_horario, name='eliminar_horario'),
    path('editar/<int:clave>', views.editar_horario, name='editar_horario'),
]
