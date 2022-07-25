from django.db import models


class News(models.Model):
    header = models.CharField('Заголовок', max_length=50)
    body = models.TextField('Основной текст')
    date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
