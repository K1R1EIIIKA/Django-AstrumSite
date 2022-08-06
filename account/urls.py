from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account_home'),
    path('register', views.register, name='register'),
    path('login', views.login_acc, name='login'),
    path('password_change', views.password_change, name='password_change'),
    path('settings', views.settings, name='settings'),
    path('profile/<username>', views.view_profile, name='profile_detail'),
]
