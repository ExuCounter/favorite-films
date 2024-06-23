from django.urls import path
from films.views import add_film

urlpatterns = [
    path('add', add_film)
]
