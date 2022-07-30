from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account_home'),
    path('login', views.login),
    path('register', views.register),
]
