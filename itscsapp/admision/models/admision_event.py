from itscsapp.events.models.event import EventModel
from django.db import models
from itscsapp.utils.models import ITSModel


class AdmisionEvent(ITSModel):
    first_name = models.CharField(max_length=70, verbose_name='Nombre')
    last_name = models.CharField(max_length=70, verbose_name='Apellido')
    phone = models.CharField(max_length=20, verbose_name='Numero Telefonico')
    email = models.EmailField(verbose_name='Email')
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name='Carrera Solicitada' )

    class Meta:
        verbose_name = 'Admision de Evento'
        verbose_name_plural = 'Admisiones de Evento'
        ordering = ['-created']

    def __str__(self):
        return self.first_name

