from django.db import models
import os

# Create your models here.

class misServicios(models.Model):
    titulo = models.CharField(max_length=20)
    descrpcion = models.CharField(max_length=225)
    imagen = models.FileField(upload_to='servicios')
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    activo = models.NullBooleanField()

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo



