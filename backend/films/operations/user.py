from films.models import User


class UserOperationException(BaseException):
    ...


class UserOperation:
    def get_instance_by_id(self, id) -> User:
        return User.objects.get(id=id)
