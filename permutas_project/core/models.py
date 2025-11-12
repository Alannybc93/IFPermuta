from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PROF', 'Professor'),
        ('COORD', 'Coordenador'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='PROF')

    def __str__(self):
        return self.username
