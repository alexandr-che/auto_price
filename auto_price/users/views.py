from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect, render
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from adverts.models import Advert, FavoriteAdvert


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'Добро пожаловать {user.username}!')
                return redirect(reverse('index:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index:index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            user = form.instance #получить все поля пользователя
            auth.login(request, user)
            messages.success(request, f'Добро пожаловать {user.username}!')
            return redirect(reverse('index:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'users/register.html', context)

@login_required(redirect_field_name='')
def profile(request, username=None):

    all_usernames = [i.get('username') for i in User.objects.all().values('username')]

    if not username:
        if request.method == 'POST':
            form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                form.save()
                redirect(reverse('users:profile'))
        else:
            form = UserProfileForm(instance=request.user)

        favorites_ad = FavoriteAdvert.objects.filter(user=request.user)
        user_ad = Advert.objects.filter(user=request.user)

        context = {
            'title': 'Личный кабинет',
            'form': form,
            'favorites_ad': favorites_ad,
            'user_ad': user_ad,
            }

        return render(request, 'users/profile.html', context)
    
    elif username in all_usernames:       
        user = User.objects.get(username=username)
        user_ad = Advert.objects.filter(user=user)

        context = {
            'title': 'Личный кабинет',
            'user': user,
            'user_ad': user_ad,
            }
        
        return render(request, 'users/other_user_profile.html', context)
    
    else:
        raise Http404
