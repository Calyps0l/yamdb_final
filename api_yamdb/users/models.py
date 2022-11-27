from api.roles import ALL_USER_ROLES
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    role = models.CharField(
        max_length=15,
        choices=ALL_USER_ROLES,
        default='user'
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        unique=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
