from django.db import models

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)


class Director(models.Model):
    class Meta:
        verbose_name = 'Директоры'
        verbose_name_plural = 'Директоры'

    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=100, null=True, verbose_name='Название:')
    rating = models.IntegerField(null=True, choices=STARS, verbose_name='Рейтинг:')
    duration = models.IntegerField(null=True, verbose_name='Длительность:')
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE, verbose_name='Директор:')

    def __str__(self):
        return self.title
