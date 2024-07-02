from django.urls import path
from films.views import LoginView

print(LoginView.as_view)

urlpatterns = [
    path('login', LoginView.as_view())
]
