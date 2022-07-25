from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news})


def shop(request):
    return render(request, 'main/shop.html')


def download(request):
    return render(request, 'main/download.html')


def about(request):
    return render(request, 'main/about.html')
