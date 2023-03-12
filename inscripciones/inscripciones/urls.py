
from django.contrib import admin
from django.urls import path, include
from materias.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programas/', include('programas_academicos.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls_materias')),
    path('', Bienvenida.as_view(), name='bienvenida'),
    path('horarios/', include('horarios.urls_horarios')),
    
    
    
]
