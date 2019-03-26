from itscsapp.utils.models import ITSModel
from django.db import models


class Facility(ITSModel):
    title = models.CharField(max_length=120, verbose_name='Titulo de la ayuda')
    image = models.ImageField(upload_to='facilities/img', verbose_name='Imagen referencial')
    description = models.TextField(verbose_name='Descripcion de la ayuda')

    class Meta:
        verbose_name = 'Facilidad y Ayuda'
        verbose_name_plural = 'Facilidades y Ayudas'
        ordering = ['-created']

    def __str__(self):
        return self.title
