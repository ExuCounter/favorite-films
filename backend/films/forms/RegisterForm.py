from django import forms
from django.core import validators
from films.operations.auth import AuthOperation


class RegisterForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your username'}), label="Login", validators=[validators.MinLengthValidator(limit_value=3, message="Login should be at least 3 characters"), validators.MaxLengthValidator(limit_value=50, message="Login should be at most 50 characters")])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'your password'}), label="Password", validators=[validators.MinLengthValidator(limit_value=5, message="Login should be at least 5 characters")])

    def __init__(self, *args, **kwargs):
        self.auth_operation = AuthOperation()
        super().__init__(*args, **kwargs)

    def sign_up(self, request):
        login = self.cleaned_data["login"]
        password = self.cleaned_data["password"]

        self.auth_operation.sign_up(login=login, password=password)
        self.auth_operation.login(request=request, login=login, password=password)
