from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import ListOfGames


class LoginForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


def validate_username(value):
    if get_user_model().objects.filter(username=value).exists():
        raise ValidationError("This name is already taken")


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", validators=[validate_username])
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["password"] != cleaned_data["password2"]:
            raise forms.ValidationError("Passwords do not match")


class GameAddForm(ModelForm):
    class Meta:
        model = ListOfGames
        fields = '__all__'
