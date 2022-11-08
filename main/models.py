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
    title = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(null=True, choices=STARS)
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
