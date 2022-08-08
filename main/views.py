from django.shortcuts import render, redirect
from .models import News
from django.template.defaulttags import register
from .forms import NewsForm
from account.funcs import get_player


def layout(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id)
        }
        return render(request, 'main/layout.html', data)
    else:
        return render(request, 'main/layout.html')


def index(request):
    new = News.objects.order_by('-date')
    if request.user.is_authenticated:
        data = {
            'news': new,
            'player': get_player(request.user.id)
        }
    else:
        data = {
            'news': new,
        }
    return render(request, 'main/index.html', data)


def shop(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id)
        }
        return render(request, 'main/shop.html', data)
    else:
        return render(request, 'main/shop.html')


def download(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id)
        }
        return render(request, 'main/download.html', data)
    else:
        return render(request, 'main/download.html')


def about(request):
    if request.user.is_authenticated:
        data = {
            'player': get_player(request.user.id)
        }
        return render(request, 'main/about.html', data)
    else:
        return render(request, 'main/about.html')


def news(request):
    new = News.objects.order_by('-date')
    if request.user.is_authenticated:
        data = {
            'news': new,
            'player': get_player(request.user.id)
        }
    else:
        data = {
            'news': new,
        }
    return render(request, 'main/news/news.html', data)


def create(request):
    if not request.user.is_staff:
        return redirect('home')
    else:
        error = ''
        if request.method == 'POST':
            form = NewsForm(request.POST)
            if form.is_valid():
                form.save()

            else:
                error = 'Неверная форма'

        form = NewsForm()
        if request.user.is_authenticated:
            data = {
                'form': form,
                'error': error,
                'player': get_player(request.user.id)
            }
        else:
            data = {
                'form': form,
                'error': error,
            }
        return render(request, 'main/news/create.html', data)


@register.filter
def list_cut_three(value):
    return value[:3]
