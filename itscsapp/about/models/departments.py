from itscsapp.utils.models import ITSModel
from django.db import models


class Department(ITSModel):
    title = models.CharField(max_length=120, verbose_name='Titulo del deparamento')
    image = models.ImageField(upload_to='facilities/img', verbose_name='Imagen referencial')
    description = models.TextField(verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['-created']

    def __str__(self):
        return self.title
