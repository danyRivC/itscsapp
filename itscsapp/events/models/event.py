from django.db import models
from itscsapp.utils.models import ITSModel
from django.shortcuts import reverse

class EventModel(ITSModel ):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    date_init = models.DateTimeField(verbose_name='Fecha de inicio del evento')
    date_finished = models.DateTimeField(verbose_name='Fecha final del evento')
    image = models.ImageField(upload_to='events', verbose_name='Imagen Representativa')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("admision-event",
                       kwargs={
                           'pk': self.pk,
                           'slug': self.slug,
                       })

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-date_init']

    def __str__(self):
        return self.title

