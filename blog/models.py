from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="blog/images/")
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'''"{self.title}" --- {self.date}'''
