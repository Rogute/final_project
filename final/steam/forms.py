from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


def validate_username(value):
    if get_user_model().objects.filter(username=value).exists():
        raise ValidationError("Nazwa zajęta")


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", validators=[validate_username])
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)
    # first_name = forms.CharField(label="First Name")
    # last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="E-mail")

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["password"] != cleaned_data["password2"]:
            raise forms.ValidationError("Passwords do not match")
