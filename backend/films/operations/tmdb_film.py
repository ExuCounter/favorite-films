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

    def add_to_favorites(self, tmdb_id):
        return TmdbFilm.objects.create(tmdb_id)

    def remove_from_favorites(self, tmdb_id):
        film = TmdbFilm.objects.get(id=tmdb_id)
        return film.delete()
