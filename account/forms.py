from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
