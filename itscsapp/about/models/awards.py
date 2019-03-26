from itscsapp.utils.models import ITSModel
from django.db import models


class Awards(ITSModel):
    title = models.CharField(max_length=120, verbose_name='Titulo del premio')
    image = models.ImageField(upload_to='awards/icons', verbose_name='Icono referencial')
    description = models.TextField(verbose_name='Descripcion del premio')
    date = models.DateField(help_text='Fecha que se otorgo el reconocimiento')

    class Meta:
        verbose_name = 'Premios'
        verbose_name_plural = 'Premios'
        ordering = ['-created']

    def __str__(self):
        return self.title

