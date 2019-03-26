from django.db import models
from django.conf import settings
from itscsapp.utils.models import ITSModel
from itscsapp.carrers.models.carrer import Carrer


class Comment(ITSModel):
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    carrer = models.ForeignKey(
        Carrer,
        related_name='comments',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content[:23]
