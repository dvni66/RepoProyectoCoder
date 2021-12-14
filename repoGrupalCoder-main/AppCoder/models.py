from django.db import models

CATEGORIA = (
    ('A', 'ACCION'),
    ('S', 'SUSPENSO'),
    ('S', 'SCIFI'),
    ('R', 'ROMANCE'),
)

IDIOMA = (
    ('ES', 'ESPAÑOL'),
    ('EN', 'INGLES'),
)

ESTADO = (
    ('AG', 'AGREGADO RECIENTE'),
    ('MO', 'MAS OBSERVADO'),
    ('MV', 'MAYOR VALORACION'),

)

class MovieInfo(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORIA, max_length=1)
    idioma = models.CharField(choices=IDIOMA, max_length=2)
    estado = models.CharField(choices=ESTADO, max_length=2)
    prodYear = models.DateField()
    viewsCount = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo



