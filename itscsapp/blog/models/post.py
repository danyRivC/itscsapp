from django.db import models
from itscsapp.utils.models import ITSModel
from django.shortcuts import reverse

class PostBlog(ITSModel):
    title = models.CharField(max_length=70, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    slug = models.SlugField
    image = models.ImageField(upload_to='blog/post', verbose_name='Imagen')
    created = models.DateField(auto_now=True , verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, verbose_name='Ultima fecha de actualizacion')

    def get_absolute_url(self):
        return reverse("courseDetail",
                       kwargs={
                           'pk': self.pk,
                           'slug': self.slug,
                       })

    class Meta:
        verbose_name_plural = 'Entradas del Blog'
        verbose_name = 'Entrada de Blog'


    def __str__(self):
        return self.title

