from itscsapp.utils.models import ITSModel
from django.db import models
from itscsapp.carrers.models import Carrer


class AdmisionCarrer(ITSModel):
    first_name = models.CharField(max_length=70, verbose_name='Nombre')
    last_name = models.CharField(max_length=70, verbose_name='Apellido')
    phone = models.CharField(max_length=20, verbose_name='Numero Telefonico')
    email = models.EmailField(verbose_name='Email')
    carrer = models.ForeignKey(Carrer, on_delete=models.CASCADE, verbose_name='Carrera Solicitada' )

    class Meta:
        verbose_name = 'Admision de Carrera'
        verbose_name_plural = 'Admisiones de Carrera'
        ordering = ['-created']

    def __str__(self):
        return self.first_name

