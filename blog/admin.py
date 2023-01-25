from django.contrib import admin
from .models import Post, ModelCategory, Like

admin.site.register(Post)
admin.site.register(ModelCategory, admin.ModelAdmin)
admin.site.register(Like)
