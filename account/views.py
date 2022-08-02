from django.shortcuts import render, redirect
from .forms import CreateUserForm, Authenticate
from django.contrib.auth import authenticate, login


def account(request):
    return render(request, 'account/account.html')


def register(request):
    error = ''
    form = CreateUserForm()

    if request.method == 'POST':
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
                return redirect('account_home')
        else:
            error = 'Неправильно введенные данные'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/login.html', data)
