from django.shortcuts import render
from .models import News
from django.template.defaulttags import register
from .forms import NewsForm


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
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Неверная форма'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/news/create.html', data)


@register.filter
def list_cut_three(value):
    return value[:3]
