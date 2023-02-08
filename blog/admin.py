from django.contrib import admin
from .models import Post, Category, Like

admin.site.site_url = '/blog/'
admin.site.register(Post)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Like)
