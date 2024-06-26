from django.urls import path
import films.views as views

urlpatterns = [
    path('home', views.home),
    path('register', views.register),
    path('login', views.login)
]
