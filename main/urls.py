from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('download', views.download, name='download'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('news/create', views.create, name='news_create'),
]
