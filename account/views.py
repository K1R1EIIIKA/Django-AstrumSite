from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm, Authenticate, CreatePlayer, ChangePasswordForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from .models import Player
from django.shortcuts import get_object_or_404
from .funcs import get_player


@login_required(login_url='login')
def account(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id)
        }
        return render(request, 'account/account.html', data)
    else:
        return redirect('login')


def view_profile(request, username):
    player = get_object_or_404(Player, username=username)
    data = {
        'player': player
    }
    return render(request, 'account/profile.html', data)


@login_required(login_url='login')
def settings(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id),
        }
        return render(request, 'account/settings.html', data)
    else:
        return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = CreateUserForm()

        if request.method == 'POST':
            forma = CreatePlayer(request.POST)
            if forma.is_valid():
                forma.save()
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('account_home')
            else:
                error = 'Неправильно введенные данные'

        data = {
            'form': form,
            'error': error
        }
        return render(request, 'registration/register.html', data)


def login_acc(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = Authenticate()
        if request.method == 'POST':
            form = Authenticate(data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                error = 'Неправильно введенные данные'
        data = {
            'form': form,
            'error': error,
        }
    return render(request, 'registration/login.html', data)


@login_required(login_url='login')
def password_change(request):
    if request.user.is_authenticated:
        error = ''
        form = ChangePasswordForm(request.user)
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('password_change_done')
            else:
                error = 'Форма заполнена неверно'

        data = {
            'form': form,
            'error': error,
            'player': get_player(request.user.id)
        }
        return render(request, 'registration/password_change_form.html', data)
    else:
        return redirect('login')


@login_required(login_url='login')
def password_change_done(request):
    data = {
        'player': get_player(request.user.id)
    }
    return render(request, 'registration/password_change_done.html', data)


@login_required(login_url='login')
def logout_acc(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


@login_required(login_url='login')
def avatar_change(request):
    error = ''
    if request.user.is_authenticated:
        pl = get_player(request.user.id)
        form = CreatePlayer(instance=pl)
        if request.method == 'POST':
            form = CreatePlayer(request.POST, request.FILES, instance=pl)
            if form.is_valid():
                form.save()
            else:
                error = 'Неправильно введенные данные'
        data = {
            'player': get_player(request.user.id),
            'form': form,
            'error': error
        }
        return render(request, 'account/avatar_change.html', data)
    else:
        return redirect('login')
