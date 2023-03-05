
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programas/', include('programas_academicos.urls_programas')),
    path('unidades/', include('unidades_academicas.urls_unidades')),
    path('materias/', include('materias.urls_materias')),
    
    
]
