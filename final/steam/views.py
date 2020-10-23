from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ListOfGames
from .forms import LoginForm, RegisterForm, GameAddForm
from bs4 import BeautifulSoup
import urllib.request


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


def get_id(link):
    new_link = ''.join((ch if ch in '0123456789' else ' ') for ch in link)
    list_of_numbers = [int(i) for i in new_link.split()]
    link = 'https://steamcommunity.com/app/' + str(list_of_numbers[0])
    return link


class GameView(View):
    def get(self, request, game_id):
        # get object link
        game = get_object_or_404(ListOfGames, id=game_id)
        url = game.link

        # get developer and publisher for object
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        developers_list = []
        developers = soup.find('div', attrs={'class': 'dev_row'})
        publishers = developers.find_next('div', attrs={'class': 'dev_row'})
        for developer in developers.find_all('a'):
            developers_list.append(developer.text)
        publisher_name = publishers.find('a').text

        # get players for object
        url = get_id(url)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        players = soup.find('span', attrs={'class': 'apphub_NumInApp'})
        players_online = players.text

        ctx = {"game": game,
               "developers": developers_list,
               "publisher": publisher_name,
               "players": players_online}
        return render(request, "game.html", ctx)
