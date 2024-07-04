from django import forms
from films.operations.auth import AuthOperation


class RegisterForm(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password")

    def __init__(self, *args, **kwargs):
        self.auth_operation = AuthOperation()
        super().__init__(*args, **kwargs)

    def sign_up(self, request):
        login = self.cleaned_data["login"]
        password = self.cleaned_data["password"]

        self.auth_operation.sign_up(login=login, password=password)
        self.auth_operation.login(request=request, login=login, password=password)
