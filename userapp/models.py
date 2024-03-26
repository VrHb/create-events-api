from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from event_app.models import Organization
from .managers import CustomUserManager


class User(AbstractUser):
    '''Сотрудник организации'''
    username = None
    email = models.EmailField(
        'Электронная почта',
        unique=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        region='RU',
        blank=True
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        related_name='users',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
