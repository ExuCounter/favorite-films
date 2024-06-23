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


class AuthorFactory(BaseFactory):
    class Meta:
        model = models.Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class FilmFactory(BaseFactory):
    class Meta:
        model = models.Film

    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence", nb_words=20)
    author = factory.SubFactory(AuthorFactory)
    user = factory.SubFactory(UserFactory)


class ActorFactory(BaseFactory):
    class Meta:
        model = models.Film

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    films = factory.RelatedFactory(FilmFactory)


class CommentFactory(BaseFactory):
    class Meta:
        model = models.Film

    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence", nb_words=20)
