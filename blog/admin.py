from django.contrib import admin
from .models import Post, ModelCategory

admin.site.register(Post)
admin.site.register(ModelCategory, admin.ModelAdmin)
