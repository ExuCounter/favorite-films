from django.urls import path
from films.views import LoginView, HomeView, RegisterView, logout, search, FilmView, toggle_favorite, FavoritesView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('logout', logout, name='logout'),
    path('toggle-favorite', toggle_favorite, name='toggle_favorite'),
    path('favorites', FavoritesView.as_view(), name='favorites'),
    path('search', search, name='search'),
    path('films/<str:id>', FilmView.as_view(), name='films')
]
