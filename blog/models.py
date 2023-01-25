from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class ModelCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название категории", unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


# TODO default datetime
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(max_length=1000, verbose_name="Основной текст")
    summary = ''
    image = models.ImageField(
        upload_to="blog/images/",
        default="",
        verbose_name="Фотография к посту",
        blank=True
    )
    date = models.DateField(verbose_name="Дата публикации", default=datetime.now)
    time = models.TimeField(verbose_name="Время публикации")
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="posts",
        on_delete=models.CASCADE,
        default=123
    )
    category = models.ForeignKey(
        to=ModelCategory,
        verbose_name="Категория",
        related_name="cat_posts",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    likes = models.ManyToManyField(
        to=User,
        related_name="post_likes",
        verbose_name="Лайкнуть",
        null=True
    )

    def __str__(self):
        return f'''"{self.title}" --- {self.date}'''


class Like(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Пользователю {self.user} понравился пост {self.post}"
