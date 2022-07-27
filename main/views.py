from django.shortcuts import render
from .models import News
from django.template.defaulttags import register


def index(request):
    new = News.objects.order_by('-date')
    return render(request, 'main/index.html', {'news': new})


def shop(request):
    return render(request, 'main/shop.html')


def download(request):
    return render(request, 'main/download.html')


def about(request):
    return render(request, 'main/about.html')


def news(request):
    new = News.objects.order_by('-date')
    return render(request, 'main/news/news.html', {'news': new})


def create(request):
    return render(request, 'main/news/create.html')


def account(request):
    return render(request, 'main/account.html')


@register.filter
def list_cut_three(value):
    return value[:3]
