from django.db import models

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(null=True, choices=STARS)
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
