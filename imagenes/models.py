from django.db import models
from django.contrib.auth.models import User

class ImagenMedica(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    url_bucket = models.URLField()
    fecha_subida = models.DateTimeField(auto_now_add=True)
    tipo_imagen = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
