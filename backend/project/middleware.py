import jwt
from django.utils.deprecation import MiddlewareMixin
from films.models import User


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Extract the token from the Authorization header
        token = request.session.get("Authorization", None)

        if token is None:
            pass

        try:
            claims = jwt.decode(token, "secret", algorithms=['HS256'])
            user_id = claims.get('user_id')

            if user_id:
                try:
                    user = User.objects.get(id=user_id)
                    request.user = {"id": user.id, "login": user.login}
                except User.DoesNotExist:
                    pass

        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass
