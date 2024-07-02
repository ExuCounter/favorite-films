from films.forms.LoginForm import LoginForm
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = "films/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.sign_in()
        return super().form_valid(form)
