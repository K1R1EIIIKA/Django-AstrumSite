from django.shortcuts import render
from .forms import CreateUserForm


def account(request):
    return render(request, 'account/account.html')


def login(request):
    return render(request, 'account/login.html')


def register(request):
    error = ''
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неправильно введенные данные'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'account/register.html', data)
