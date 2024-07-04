from django.db import models

# Create your models here.


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def __repr__(self):
        return f"User(login='{self.login}')"


class TmdbFilm(models.Model):
    tmdb_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"TmdbFilm(tmdb_id='{self.tmdb_id}', user='{self.user.__repr__()}')"


class Comment(models.Model):
    text = models.TextField()
    film = models.ForeignKey(TmdbFilm, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Comment(text='{self.text}', user='{self.film.__repr__()}')"
