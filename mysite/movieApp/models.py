from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)
    tmdb_id = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    img_path = models.URLField(null=True, blank=True)

    # rolefK = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=128, null=True, blank=True)
    release_date = models.DateField()

    description = models.TextField(null=True, blank=True)
    studiofK = models.ForeignKey(
        Studio, on_delete=models.CASCADE, blank=True, null=True
    )
    duration = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=128, blank=True)
    tmdb_id = models.IntegerField(blank=True, null=True, unique=True)
    img_path = models.URLField(null=True, blank=True)
    genresfK = models.ManyToManyField(Genre)
    credits = models.ManyToManyField(Person, through="MovieCredit")

    def __str__(self):
        return self.title


class MovieCredit(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title}: {self.person.name} ({self.role.name})"


class MovieReview(models.Model):
    userfK = models.ForeignKey(User, on_delete=models.CASCADE)
    moviefK = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    review = models.TextField(blank=True)
