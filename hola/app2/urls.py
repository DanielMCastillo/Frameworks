from django.urls import path
from app2 import views

urlpatterns = [
    path('hola/', views.hola),
    path('mensaje/', views.mensaje),
]
