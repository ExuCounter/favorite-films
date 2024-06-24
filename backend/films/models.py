from django.db import models
from django.forms.models import model_to_dict

# Create your models here.


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    def __repr__(self):
        return f"User(login='{self.login}')"


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f"Author(first_name='{self.first_name}', last_name='{self.last_name}')"


class TmdbFilm(models.Model):
    tmdb_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"TmdbFilm(tmdb_id='{self.tmdb_id}', user='{self.user.__repr__()}')"


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def clone(self):
        film_dict = model_to_dict(self, exclude=['_state'])
        return Film(**film_dict)

    def __repr__(self):
        return f"Film(name='{self.name}', description='{self.description}', author='{self.author.__repr__()}', user='{self.user.__repr__()}')"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    films = models.ManyToManyField(Film)

    def __repr__(self):
        return f"Actor(first_name='{self.first_name}', last_name='{self.last_name}', films='{self.films}')"


class Comment(models.Model):
    text = models.TextField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
