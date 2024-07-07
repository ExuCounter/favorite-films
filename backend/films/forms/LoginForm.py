from django import forms
from films.operations.auth import AuthOperation, AuthOperationException


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your username'}), label="Login")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'your password'}), label="Password")

    def __init__(self, *args, **kwargs):
        self.auth_operation = AuthOperation()
        super().__init__(*args, **kwargs)

    def sign_in(self, request):
        login = self.cleaned_data["login"]
        password = self.cleaned_data["password"]

        try:
            self.auth_operation.login(request=request, login=login, password=password)

            return "ok"
        except AuthOperationException:
            return forms.ValidationError("Invalid login or username")
