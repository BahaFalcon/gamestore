from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Модель для пользователя"""
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    email = models.CharField('Эл.почта', max_length=255, unique=True)
    password = models.CharField('Пароль', max_length=255)
    username = models.CharField(max_length=150, unique=True)
    location = models.CharField('Адрес', max_length=30, blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Номер телефона', validators=[phoneNumberRegex], max_length=15, unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

