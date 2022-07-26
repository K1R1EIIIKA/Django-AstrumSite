from django.shortcuts import render
from .models import News
from django.template.defaulttags import register


def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news})


def shop(request):
    return render(request, 'main/shop.html')


def download(request):
    return render(request, 'main/download.html')


def about(request):
    return render(request, 'main/about.html')


def news_all(request):
    news = News.objects.all()
    return render(request, 'main/news_all.html', {'news': news})


@register.filter
def list_cut_three(value):
    return value[:3]
