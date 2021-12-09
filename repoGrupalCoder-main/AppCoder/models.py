from django.db import models

class MovieInfo(models.Model):
    clasificacion = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    lenguajeOriginal = models.CharField(max_length=10)
    director = models.CharField(max_length=40)
    productor = models.CharField(max_length=40)
    escritor = models.CharField(max_length=40)
    fechaEstreno = models.DateField()
    fechaStreaming = models.DateField()
    duracion = models.IntegerField()
    distribuidor = models.CharField(max_length=40)


