from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# class AuthorUser(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username


# TODO default datetime
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(max_length=1000, verbose_name="Основной текст")
    summary = ''
    image = models.ImageField(upload_to="blog/images/", default="", verbose_name="Фотография к посту")
    date = models.DateField(verbose_name="Дата публикации", default=datetime.now)
    time = models.TimeField(verbose_name="Время публикации")
    author = models.ForeignKey(
        User,
        verbose_name="User",
        related_name="posts",
        on_delete=models.CASCADE,
        default=123
    )

    def __str__(self):
        return f'''"{self.title}" --- {self.date}'''
