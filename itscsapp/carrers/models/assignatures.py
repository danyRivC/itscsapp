from django.db import models
from itscsapp.utils.models import ITSModel
from itscsapp.carrers.models.carrer import Carrer
from itscsapp.carrers.models.semesters import Semester


class Asignature(ITSModel):
    carrer = models.ManyToManyField(Carrer, verbose_name='Carrera', related_name='get_carrer')
    name_assignature = models.CharField(max_length=255, verbose_name='Materia')
    cicle = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name='Semestre Asignado')

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['-created']

    def __str__(self):
        return self.name_assignature
