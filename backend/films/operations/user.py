from films.models import User
from argon2 import PasswordHasher

ph = PasswordHasher()


class UserException(BaseException):
    ...


class UserOperation:
    def get_instance_by_id(self, id):
        return User.objects.get(id=id)

    def register(self, login, password):
        try:
            password_hash = ph.hash("correct horse battery staple")
            user = User(login=login, password=password_hash)
            user.save()
        except ValueError:
            return UserException("Can't register user")

    def login(self, login, password):
        try:
            user = User.objects.get(login=login)
            if ph.verify(user.password, password):
                user.save()
            else:
                raise ValueError("Wrong password")
        except ValueError:
            return UserException("Can't login user")
