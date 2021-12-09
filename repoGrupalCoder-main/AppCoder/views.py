from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def accion(request):
    return render(request, 'AppCoder/accion.html')


def romance(request):
    return render(request, 'AppCoder/romance.html')


def terror(request):
    return render(request, 'AppCoder/terror.html')


def suspenso(request):
    return render(request, 'AppCoder/suspenso.html')

def estrenos(request):
    return render(request, 'AppCoder/estrenos.html')
