from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import PeliForm
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def accion(request):
    return render(request, 'AppCoder/accion.html')


def romance(request):
    return render(request, 'AppCoder/romance.html')


def scifi(request):
    return render(request, 'AppCoder/scifi.html')


def suspenso(request):
    return render(request, 'AppCoder/suspenso.html')

def estrenos(request):
    return render(request, 'AppCoder/estrenos.html')

def oblivion(request):
    return render(request, 'AppCoder/oblivion.html')

def revenant(request):
    return render(request, 'AppCoder/revenant.html')

def diehard(request):
    return render(request, 'AppCoder/diehard.html')
    
def thewalk(request):
    return render(request, 'AppCoder/thewalk.html')

    
def peliform(request):
    if request.method == "POST":
        miFormulario = PeliForm(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            peliInfo = PeliForm(
                                    titulo = info["titulo"],
                                    descripcion = info["descripcion"],
                                    categoria = info["categoria"],
                                    idioma = info["idioma"],
                                    estado = info["estado"],
                                    cast = info["cast"],
                                    prodYear = info["prodYear"],
                                )
            peliInfo.save()

            return render(request,  'AppCoder/inicio.html')
    else:
        miFormulario = PeliForm()

    return render(request, 'AppCoder/peliform.html', {"miFormulario":miFormulario})