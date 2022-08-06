from django.forms import TextInput, EmailInput, CharField, PasswordInput, ModelForm
from django.contrib.auth.models import User
from .models import Player
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Ваш игровой никнейм'
            }),
            'email': EmailInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Пример: huykekasa@gmail.com'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-account-control'
        self.fields['password2'].widget.attrs['class'] = 'form-account-control'


class Authenticate(AuthenticationForm):
    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(Authenticate, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={'class': 'form-account-control',
               'placeholder': 'ник'
               }))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
            'placeholder': 'пароль',
        }))


class CreatePlayer(ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(CreatePlayer, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={'class': 'form-account-control',
               'placeholder': 'ник'
               }))
    email = CharField(widget=EmailInput(
        attrs={'class': 'form-account-control',
               'placeholder': 'емэйл'
               }))


class ChangePasswordForm(PasswordChangeForm):
    fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
        }))
    new_password1 = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
        }))
    new_password2 = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
        }))
