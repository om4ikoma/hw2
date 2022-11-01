from django.db import models

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)
# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, choices=STARS)
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.title

