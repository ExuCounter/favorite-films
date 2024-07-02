from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password")

    def sign_in(self):
        pass
