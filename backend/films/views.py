from films.forms.LoginForm import LoginForm
from films.forms.RegisterForm import RegisterForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, JsonResponse
from films.forms.LogoutForm import LogoutForm
from films.operations.tmdb_film import TmdbFilmOperation
from django.urls import reverse
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context["user"] = self.request.GET["user"] or None
        except KeyError:
            ...

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


def search(request):
    if request.method == "POST":
        tmdb_film_operation = TmdbFilmOperation()
        body = json.loads(request.body)

        if len(body["query"]) > 2:
            data = tmdb_film_operation.search(query=body["query"], limit=body["limit"] or 10)
            return JsonResponse({"films": data})
        else:
            return JsonResponse({"films": []})
