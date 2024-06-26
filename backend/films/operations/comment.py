import tvdb_v4_official
from project.settings import TMDB_API_TOKEN
from films.models import Comment


class TmdbFilmOperationException(BaseException):
    ...

class CommentOperation:
    ...
