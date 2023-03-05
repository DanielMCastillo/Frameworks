from django.urls import path
from materias import views

urlpatterns = [
    path('', views.ListaMaterias.as_view(), name='lista_programas'),
    
    
]