from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name = "Inicio"),
    path('estrenos', views.estrenos, name = "Estrenos"),
    path('accion', views.accion, name = "Accion"),
    path('romance', views.romance, name = "Romance"),
    path('scifi', views.scifi, name = "Scifi"),
    path('suspenso', views.suspenso, name = "Suspenso"),
    path('oblivion', views.oblivion, name= "Oblivion"),
    path('revenant', views.revenant, name= "Revenant"),
    path('diehard', views.diehard, name = "DieHard"),
    path('thewalk', views.diehard, name = "TheWalk"),
]


