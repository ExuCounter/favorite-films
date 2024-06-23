from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    films = models.ManyToManyField(Film)


class Comment(models.Model):
    text = models.TextField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
