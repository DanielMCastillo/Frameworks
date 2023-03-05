from django.urls import path
from cal2 import views

urlpatterns = [
    path('sumar', views.sumar),
]
