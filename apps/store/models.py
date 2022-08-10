from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Genre(models.Model):
    """Модель для жанров"""
    title = models.CharField('Жанр', max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Game(models.Model):
    """Модель для игр"""
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', upload_to='image/')
    genres = models.ManyToManyField(Genre, related_name='games', verbose_name='Жанры')
    description = RichTextUploadingField('Описание')
    video_url = models.URLField(verbose_name='Ссылка на видео', max_length=200, blank='False', null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name
