from films.operations.user import UserOperation
import films.tests.factory as factory
import pytest


@pytest.mark.django_db
def test_user_authentication():
    user = factory.UserFactory.build()
    user_operation = UserOperation()

    user_operation.sign_up(login=user.login, password=user.password)
    authenticated = user_operation.authenticate(login=user.login, password=user.password)
    not_authenticated1 = user_operation.authenticate(login=user.login, password="other password")
    not_authenticated2 = user_operation.authenticate(login="other_login", password=user.password)

    assert authenticated
    assert not_authenticated1 is False
    assert not_authenticated2 is False
