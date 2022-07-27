from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('download', views.download),
    path('about', views.about),
    path('news', views.news),
    path('news/create', views.create),
    path('account', views.account),
]
