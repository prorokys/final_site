from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label="Введіть ім'я користувача",
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введіть ім'я користувача",
    #         }
    #     ),
    # )
    # password = forms.CharField(
    #     label="Введіть пароль",
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": True,
    #             "class": "form-control",
    #             "placeholder": "Введіть пароль",
    #         }
    #     ),
    # )

    class Meta:
        model = User
        fields = ("username", "password")
