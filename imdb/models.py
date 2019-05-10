from django.db import models


class Actor(models.Model):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=16, blank=True, null=True)
    death_year = models.CharField(max_length=16, blank=True, null=True)
    profession = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    name = models.TextField(blank=True, null=True)
    type_title = models.CharField(max_length=64, blank=True, null=True)
    is_adult = models.BooleanField(null=True)
    start_year = models.CharField(max_length=16, blank=True, null=True)
    end_year = models.CharField(max_length=16, blank=True, null=True)
    run_time = models.CharField(max_length=32, blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    cast = models.ManyToManyField(Actor, through='MovieCast')

    def __str__(self):
        return self.name


class MovieCast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.movie.name)
