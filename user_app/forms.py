from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model

from user_app.models import CustomUser, Company


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Введите пароль"}
        ),
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Подтвердите пароль"}
        ),
        strip=False,
    )

    company = forms.CharField(
        label="Компания",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Название компании"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        company = self.cleaned_data.get("company")
        if company:
            company, created = Company.objects.get_or_create(name=company)
            user.company = company
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username").lower()
        return username


class ProfileUpdateForm(forms.ModelForm):
    position = forms.CharField(required=False)
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "position", "company"]

        widgets = {
            "company": forms.Select(attrs={"class": "form-select"}),
        }
