from itscsapp.utils.models import ITSModel
from django.db import models
from itscsapp.carrers.models import Carrer
from django.core.validators import RegexValidator


class AdmisionCarrer(ITSModel):
    first_name = models.CharField(max_length=70, verbose_name='Nombre')
    last_name = models.CharField(max_length=70, verbose_name='Apellido')
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}',
        message="Phone number must be entered in the format +9999999999. Up to 20 digits"
    )
    phone = models.CharField(validators=[phone_regex],max_length=20, verbose_name='Numero Telefonico')
    email = models.EmailField(verbose_name='Email')
    carrer = models.ForeignKey(Carrer, on_delete=models.CASCADE, verbose_name='Carrera Solicitada' )

    class Meta:
        verbose_name = 'Admision de Carrera'
        verbose_name_plural = 'Admisiones de Carrera'
        ordering = ['-created']

    def __str__(self):
        return self.first_name

