from itscsapp.utils.models import ITSModel
from django.db import models

class Research(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.FileField(upload_to='research', verbose_name='Imagen representativa')
    created = models.DateTimeField(auto_now_add="True", verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now='True', verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'investigacion'
        verbose_name_plural = 'investigaciones'
        ordering =['-created']

    def __str__(self):
        return self.title
