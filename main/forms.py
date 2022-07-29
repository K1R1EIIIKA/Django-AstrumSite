from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['header', 'body', 'date', 'author']

        widgets = {
            'header': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Основной текст'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации (формат: гггг-мм-дд чч:мм)'
            }),
            'author': Select(attrs={
                'class': 'form-control'
            })
        }
