from django.db import models


class Organization(models.Model):
    '''Организация'''
    title = models.CharField(
        'Название',
        max_length=100
    )
    description = models.TextField(
        'Описание',
        blank=True
    )
    address = models.CharField(
        'Адрес',
        max_length=200
    )
    postcode = models.IntegerField(
        'Почтовый индекс', 
    )

    def __str__(self):
        return f'Организация - {self.title}'
    
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class Event(models.Model):
    '''Мероприятие'''
    title = models.CharField(
        'Название',
        max_length=100
    )
    description = models.TextField(
        'Описание',
        blank=True
    )
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(
        'Изображение',
        upload_to='events_images',
        blank=True,
        null=True,
    )
    date = models.DateTimeField(
        'Дата проведения',
    )

    def __str__(self):
        return f'{self.date} - {self.title}'
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
