from django.db import models
from itscsapp.utils.models import ITSModel


class Semester(ITSModel):
    number_semester = models.IntegerField(verbose_name="Numero de Semestre")
    semester_name = models.CharField(max_length=240, verbose_name="Semestre")

    class Meta:
        verbose_name = 'Semestre'
        verbose_name_plural = 'Semestres'
        ordering = ['number_semester']

    def __str__(self):
        return self.semester_name
