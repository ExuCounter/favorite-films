from films.operations.tmdb_film import TmdbFilmOperation
import unittest.mock as mock
import unittest
import tvdb_v4_official


class TmdbFilmOperationTest(unittest.TestCase):
    # Patch to allow creation of the instance without token
    @mock.patch("tvdb_v4_official.TVDB.__init__")
    def setUp(self, mock_init):
        mock_init.return_value = None
        tmdb_film_operation = TmdbFilmOperation("fake token")
        self.tmdb_film_operation = tmdb_film_operation

    # Patch to avoid real API calls, we just need to verify our code, not others
    @mock.patch.object(tvdb_v4_official.TVDB, "search")
    def test_tmdb_film_search(self, mock_search):
        kwargs = {"query": "deadpool", "limit":10}
        self.tmdb_film_operation.search(**kwargs)

        mock_search.assert_called_with(kwargs["query"])

    # Patch to avoid real API calls, we just need to verify our code, not others
    @mock.patch.object(tvdb_v4_official.TVDB, "search")
    def test_limited_search(self, mock_search):
        kwargs = {"query": "deadpool", "limit":2}
        mock_search.return_value = [{'country': 'usa'}, {'country': 'ukr'}, {'country': 'cad'}]
        result = self.tmdb_film_operation.search(**kwargs)
        mock_search.assert_called_with(kwargs["query"])

        assert result == [{'country': 'usa'}, {'country': 'ukr'}]
