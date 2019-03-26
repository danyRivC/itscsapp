from itscsapp.utils.models import ITSModel
from django.db import models


class Contact(ITSModel):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    phone_number = models.CharField(max_length=255, verbose_name='Numero De Telefono')
    subject = models.CharField(max_length=255, verbose_name='Asunto')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Mensaje')
    created = models.DateTimeField(auto_now_add="True", verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now='True', verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'contactos'
        ordering = ['-created']

    def __str__(self):
        return self.name
