from films.operations.user import UserOperation
from films.models import User
import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


class AuthOperationException(BaseException):
    ...


class AuthOperation:
    def __init__(self):
        self.user_operation = UserOperation()

    def get_token(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            authenticated_user = self.authenticate(login=login, password=password)

            if not isinstance(authenticated_user, User):
                return None

            encoded_jwt = jwt.encode({"user_id": authenticated_user.id}, "secret", algorithm="HS256")

            return encoded_jwt

    def login(self, request, login, password):
        token = self.get_token(login=login, password=password)

        if token is None:
            raise AuthOperationException("User can't be authenticated")
        else:
            request.session["Authorization"] = token

        return request

    def authenticate(self, login, password) -> User | ValueError:
        try:
            user = User.objects.get(login=login)

            if ph.verify(user.password, password):
                return user
            else:
                raise ValueError("Wrong password")
        except (ValueError, VerifyMismatchError, User.DoesNotExist):
            return ValueError("Wrong credentials")

    def sign_up(self, login, password) -> User | AuthOperationException:
        try:
            password_hash = ph.hash(password)
            user = User(login=login, password=password_hash)
            user.save()

            return user
        except ValueError:
            return AuthOperationException("Can't register user")

    def logout(self, request):
        del request.session["Authorization"]
        return request
