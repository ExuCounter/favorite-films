import factory
import films.models as models
from argon2 import PasswordHasher

ph = PasswordHasher()


class BaseFactory(factory.django.DjangoModelFactory):
    ...


class UserFactory(BaseFactory):
    class Meta:
        model = models.User

    login = factory.Faker("user_name")
    password = factory.Faker("password")


class TmdbFilmFactory(BaseFactory):
    class Meta:
        model = models.TmdbFilm

    tmdb_id = factory.Faker("id")
    user = factory.SubFactory(UserFactory)


class CommentFactory(BaseFactory):
    class Meta:
        model = models.Comment

    text = factory.Faker("sentence", nb_words=10)
    film = factory.SubFactory(TmdbFilmFactory)
