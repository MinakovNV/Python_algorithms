from django.db import models
from django.contrib.auth.models import User
from films.models import Film


class Otziv(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=20000)
    email = models.EmailField()
    date = models.DateField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE,)

    def __str__(self):
        return self.film.name

    def get_film_name(self):
        return self.film.name
