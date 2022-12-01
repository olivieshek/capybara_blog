from datetime import datetime
from django.db import models


# TODO default datetime
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(max_length=1000, verbose_name="Основной текст")
    image = models.ImageField(upload_to="blog/images/", default="", verbose_name="Фотография к посту")
    date = models.DateField(verbose_name="Дата публикации", default=datetime.now)
    time = models.TimeField(verbose_name="Время публикации")

    def __str__(self):
        return f'''"{self.title}" --- {self.date}'''
