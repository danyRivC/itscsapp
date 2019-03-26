from itscsapp.utils.models import ITSModel
from django.db import models
from .carrer import Carrer


class InformationCarrer(ITSModel):
    requirements = models.TextField(verbose_name='Requerimientos')
    costos = models.TextField(verbose_name='Costos')
    carrer = models.OneToOneField(Carrer, on_delete=models.CASCADE)
    student_profile = models.TextField(verbose_name='Perfil del estudiante')

    class Meta:
        verbose_name = 'Informacion de la carrera'
        verbose_name_plural = 'Informacion sobre las carreras'
        ordering = ['-created']

    def __str__(self):
        return self.carrer.title
