from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, get_user_model

from user_app.forms import CustomUserCreationForm, CustomAuthenticationForm
from user_app.models import CustomUser


def general(request):
    return render(request, "user_app/general.html")


class CustomRegisterView(FormView):
    template_name = "user_app/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "user_app/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class CustomListView(ListView):
    model = CustomUser
    template_name = "user_app/list_user.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        user_company = self.request.user.company
        return queryset.filter(company=user_company)


@login_required
def profile_view(request):
    user = request.user
    return render(request, "user_app/profile.html", {"user": user})
