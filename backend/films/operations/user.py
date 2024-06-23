from films.models import User
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


class UserOperationException(BaseException):
    ...


class UserOperation:
    def get_instance_by_id(self, id) -> User:
        return User.objects.get(id=id)

    def sign_up(self, login, password) -> User | UserOperationException:
        try:
            password_hash = ph.hash(password)
            user = User(login=login, password=password_hash)
            user.save()

            return user
        except ValueError:
            return UserOperationException("Can't register user")

    def authenticate(self, login, password) -> bool:
        try:
            user = User.objects.get(login=login)

            if ph.verify(user.password, password):
                return True
            else:
                raise ValueError("Wrong password")
        except (ValueError, VerifyMismatchError, User.DoesNotExist):
            return False
