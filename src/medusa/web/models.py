from django.db import models


class Post(models.Model):
    date = models.DateField('Дата')
    subject = models.CharField('Заголовок', max_length=256)
    content = models.TextField('Содержание')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.subject
