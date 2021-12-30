from django.db import models
from django.db.models.base import Model

# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres, blank = True, null = True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    description = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return self.decription
