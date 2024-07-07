import tvdb_v4_official
from project.settings import TMDB_API_TOKEN
from films.models import TmdbFilm


class TmdbFilmOperationException(BaseException):
    ...


class TmdbFilmOperation:
    def __init__(self, token=TMDB_API_TOKEN):
        if isinstance(token, str):
            self.tvdb = tvdb_v4_official.TVDB(token)
        else:
            raise TmdbFilmOperationException("tmdb token is not correct")

    def search(self, query, limit):
        result = self.tvdb.search(query)
        return result[0:limit]

    def add_to_favorites(self, tmdb_id, user_id):
        return TmdbFilm.objects.create(tmdb_id=tmdb_id, user_id=user_id)

    def remove_from_favorites(self, tmdb_id, user_id):
        film = TmdbFilm.objects.get(tmdb_id=tmdb_id, user_id=user_id)
        return film.delete()

    def toggle_favorite(self, tmdb_id, user_id) -> bool:
        if TmdbFilm.objects.filter(tmdb_id=tmdb_id, user_id=user_id).exists():
            self.remove_from_favorites(tmdb_id=tmdb_id, user_id=user_id)
            return False
        else:
            self.add_to_favorites(tmdb_id=tmdb_id, user_id=user_id)
            return True

    def get_film(self, tmdb_id):
        film = self.tvdb.get_movie(tmdb_id)
        film["is_favorite"] = TmdbFilm.objects.filter(tmdb_id=tmdb_id).exists()

        return film
