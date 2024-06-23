# from films.operations.user import UserOperation
import films.tests.factory as factory


def test_user_login():
    user = factory.UserFactory()

    user.login()

    assert 1 == 1
