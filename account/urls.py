from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account_home'),
    path('register', views.register, name='register'),
    path('login', views.login_acc, name='login'),
    path('logout', views.logout_acc, name='logout'),
    path('settings', views.settings, name='settings'),
    path('settings/avatar_change', views.avatar_change, name='avatar_change'),
    path('settings/password_change', views.password_change, name='password_change'),
    path('settings/password_change/done', views.password_change_done, name='password_change_done'),
    path('profile/<username>', views.view_profile, name='profile_detail'),
]
