from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'avatar'
        ]

    avatar = forms.ImageField(required=False)


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'avatar'
        ]

    avatar = forms.ImageField(required=False)


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль*',
                                   widget=forms.PasswordInput(
                                       attrs={
                                           'class': 'form-control'
                                       }
                                   ))
    new_password1 = forms.CharField(label='Новый пароль*',
                                   widget=forms.PasswordInput(
                                       attrs={
                                           'class': 'form-control'
                                       }
                                   ))
    new_password2 = forms.CharField(label='Повторите новый пароль*',
                                   widget=forms.PasswordInput(
                                       attrs={
                                           'class': 'form-control'
                                       }
                                   ))
    