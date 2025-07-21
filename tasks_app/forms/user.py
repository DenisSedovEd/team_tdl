from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from tasks_app.models.user import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
        help_text="Required. 30 characters or fewer.",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password", "position", "status")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
        help_text="Required. 30 characters or fewer.",
    )

    class Meta:
        model = User
        fields = ("username", "password")
