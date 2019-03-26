from django.db import models
from itscsapp.utils.models import ITSModel
from .categories import Category
from django.urls import reverse


class Carrer(ITSModel):
    title = models.CharField(max_length=100, verbose_name='Titulo de Carrera')
    description = models.TextField(verbose_name='Descripción de la Carrera')
    image = models.ImageField(upload_to='carrers', verbose_name='Imagen Representativa')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Categoria'
    )

    def get_absolute_url(self):
        return reverse("detail_view",
                       kwargs={
                           'int': self.pk,
                           'slug': self.slug
                       })

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.title

