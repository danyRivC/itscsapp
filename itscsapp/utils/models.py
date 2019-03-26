from django.db import models


class ITSModel(models.Model):
    created =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificaicon')

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', 'updated']



