from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views import View
# from .models import
from .forms import LoginForm, RegisterForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect("list/")
        return render(request, "login.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop("password2")
            user = get_user_model().objects.create_user(**form.cleaned_data)
            return redirect("login")
        return render(request, "register.html", {"form": form})
