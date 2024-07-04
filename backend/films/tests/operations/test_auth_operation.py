import unittest
from films.operations.auth import AuthOperation
import pytest
import films.tests.factory as factory
import jwt


@pytest.mark.django_db
class AuthOperationTest(unittest.TestCase):
    def setUp(self):
        self.auth_operation = AuthOperation()

    def test_token_for_non_existing_user(self):
        user = factory.UserFactory.build()
        token = self.auth_operation.get_token(login=user.login, password=user.password)

        assert token is None

    def test_token_for_existing_user(self):
        user = factory.UserFactory.build()
        signed_user = self.auth_operation.sign_up(login=user.login, password=user.password)
        token = self.auth_operation.get_token(login=user.login, password=user.password)
        claims = jwt.decode(token, "secret", algorithms=["HS256"])

        assert claims["user_id"] is signed_user.id

    @pytest.mark.django_db
    def test_user_authentication(self):
        user = factory.UserFactory.build()

        self.auth_operation.sign_up(login=user.login, password=user.password)
        authenticated_user = self.auth_operation.authenticate(login=user.login, password=user.password)
        not_authenticated_user_error1 = self.auth_operation.authenticate(login=user.login, password="other password")
        not_authenticated_user_error2 = self.auth_operation.authenticate(login="other_login", password=user.password)

        assert authenticated_user is not None
        assert isinstance(not_authenticated_user_error1, ValueError)
        assert isinstance(not_authenticated_user_error2, ValueError)
