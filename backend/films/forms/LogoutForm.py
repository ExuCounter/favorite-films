from django import forms
from films.operations.auth import AuthOperation


class LogoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.auth_operation = AuthOperation()
        super().__init__(*args, **kwargs)

    def logout(self, request):
        print(request)
        self.auth_operation.logout(request=request)
        return "ok"
