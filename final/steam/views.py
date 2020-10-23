from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ListOfGames
from .forms import LoginForm, RegisterForm, GameAddForm


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
                return redirect("main")
        return render(request, "login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("login")


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


class GameAddView(View):
    def get(self, request):
        form = GameAddForm()
        return render(request, "game_add.html", {"form": form})

    def post(self, request):
        form = GameAddForm(request.POST)
        if form.is_valid():
            game = ListOfGames.objects.create(**form.cleaned_data)
            return redirect("main")
        return render(request, "game_add.html", {"form": form})


class ListOfGamesView(View):
    def get(self, request):
        games = ListOfGames.objects.all()
        return render(request, "main.html", {"games": games})


class GameView(View):
    def get(self, request, game_id):
        game = get_object_or_404(ListOfGames, id=game_id)
        ctx = {"game": game}
        return render(request, "game.html", ctx)
