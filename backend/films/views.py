from films.forms.LoginForm import LoginForm
from films.forms.RegisterForm import RegisterForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect, JsonResponse
from films.forms.LogoutForm import LogoutForm
from films.operations.tmdb_film import TmdbFilmOperation
from django.urls import reverse
from films.models import User, TmdbFilm
import json


class LoginView(FormView):
    template_name = "films/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        status = form.sign_in(self.request)

        if status == "error":
            return HttpResponseRedirect(reverse("login"))

        return super().form_valid(form)


class RegisterView(FormView):
    template_name = "films/register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        form.sign_up(self.request)
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = "films/home.html"

    def dispatch(self, request, *args, **kwargs):
        if request.session.get("Authorization", None) is None:
            return HttpResponseRedirect(reverse("register"))

        return super().dispatch(request, *args, **kwargs)


class FavoritesView(TemplateView):
    template_name = 'films/favorites.html'
    model = TmdbFilm
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tmdb_film_operation = TmdbFilmOperation()

        user = User.objects.get(id=self.request.user["id"])
        films = list(user.tmdbfilm_set.all())

        for index, film in enumerate(films):
            films[index] = tmdb_film_operation.get_film(film.tmdb_id)

        context["films"] = films

        return context


class FilmView(TemplateView):
    template_name = "films/~id/index.html"

    def __init__(self, *args, **kwargs):
        self.tmdb_film_operation = TmdbFilmOperation()
        super().__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.tmdb_film_operation.get_film(self.kwargs["id"])

        context["film"] = film

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.session.get("Authorization", None) is None:
            return HttpResponseRedirect(reverse("register"))

        return super().dispatch(request, *args, **kwargs)


def logout(request):
    if request.method == "POST":
        form = LogoutForm()
        form.logout(request=request)

        return HttpResponseRedirect(reverse("login"))


def toggle_favorite(request):
    if request.method == "POST":
        tmdb_film_operation = TmdbFilmOperation()
        body = json.loads(request.body)
        is_favorite = tmdb_film_operation.toggle_favorite(tmdb_id=body["film_id"], user_id=request.user["id"])

        return JsonResponse({"success": True, "payload": {"is_favorite": is_favorite}})


def search(request):
    if request.method == "POST":
        tmdb_film_operation = TmdbFilmOperation()
        body = json.loads(request.body)

        if len(body["query"]) > 2:
            data = tmdb_film_operation.search(query=body["query"], limit=body["limit"] or 10)
            return JsonResponse({"films": data})
        else:
            return JsonResponse({"films": []})
