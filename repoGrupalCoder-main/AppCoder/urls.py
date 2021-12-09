from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name = "Inicio"),
    path('estrenos', views.estrenos, name = "Estrenos"),
    path('accion', views.accion, name = "Accion"),
    path('romance', views.romance, name = "Romance"),
    path('terror', views.terror, name = "Terror"),
    path('suspenso', views.suspenso, name = "Suspenso"),
    
]