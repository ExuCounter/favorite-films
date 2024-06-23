import films.tests.factory as factory
import pytest
from films.models import Film


@pytest.mark.django_db
def test_film_creation():
    film = factory.FilmFactory()

    created_film = Film.objects.get(id=film.id)

    assert created_film.name == film.name


@pytest.mark.django_db
def test_film_deletion():
    film = factory.FilmFactory()

    found_film = Film.objects.get(id=film.id)

    assert found_film.name == film.name

    found_film.delete()

    try:
        Film.objects.get(id=film.id)
    except Film.DoesNotExist:
        assert True


@pytest.mark.django_db
def test_film_update():
    film = factory.FilmFactory()

    found_film = Film.objects.get(id=film.id)

    assert found_film.name == film.name
    assert found_film.description == film.description

    new_film = factory.FilmFactory()

    found_film.name = new_film.name
    found_film.description = new_film.description

    found_film.save()

    updated_film = Film.objects.get(id=found_film.id)

    assert updated_film.name == new_film.name
    assert updated_film.description == new_film.description

    assert updated_film.name != film.name
    assert updated_film.description != film.description
