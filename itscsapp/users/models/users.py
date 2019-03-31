from django.contrib.auth.models import AbstractUser
from itscsapp.utils.models import ITSModel
from django.core.validators import RegexValidator
from django.db import models


class User(ITSModel, AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'Users already exist'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}',
        message="Phone number must be entered in the format +9999999999. Up to 20 digits"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_student = models.BooleanField(
        default=False,
        help_text=('If the user is a student, he / she will be able to enroll in the subjects')
    )

    is_verify = models.BooleanField(
        default=False,
        help_text=('That is true when the user verify your email address'),
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

