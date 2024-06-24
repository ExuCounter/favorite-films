from films.operations.tmdb_film import TmdbFilmOperation
import unittest.mock as mock
import unittest
import tvdb_v4_official


class TmdbFilmOperationTest(unittest.TestCase):
    @mock.patch.object(tvdb_v4_official.TVDB, "search")
    def test_tmdb_film_search(self, mock_search):
        kwargs = {"query": "deadpool", "limit":10}
        tmdb_film_operation = TmdbFilmOperation()
        tmdb_film_operation.search(**kwargs)

        mock_search.assert_called_with(kwargs["query"])

    @mock.patch.object(tvdb_v4_official.TVDB, "search")
    def test_limited_search(self, mock_search):
        kwargs = {"query": "deadpool", "limit":2}
        tmdb_film_operation = TmdbFilmOperation()

        mock_search.return_value = [{'country': 'usa'}, {'country': 'ukr'}, {'country': 'cad'}]
        result = tmdb_film_operation.search(**kwargs)

        mock_search.assert_called_with(kwargs["query"])

        assert result == [{'country': 'usa'}, {'country': 'ukr'}]
