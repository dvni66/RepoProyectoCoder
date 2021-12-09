from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name = "Inicio"),
    path('estrenos', views.estrenos, name = "Estrenos"),
    path('profesores', views.profesores, name = "Profesores"),
    path('estudiantes', views.estudiantes, name = "Estudiantes"),
    path('entregables', views.entregable, name = "Entregables"),
    
]