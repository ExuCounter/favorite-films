from django.urls import path
from films.views import LoginView, HomeView, RegisterView, logout, search

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('logout', logout, name='logout'),
    path('search', search, name='search')
]
