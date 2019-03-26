from django.db import models
from itscsapp.utils.models import ITSModel


class Category(ITSModel):
    name = models.CharField(max_length=255, verbose_name='Nombre Categoria')

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['-created']

    def __str__(self):
        return self.name
