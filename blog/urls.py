from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_post/", views.add_post, name="add_post"),
    path("read_post/<int:id>", views.read_post, name="read_post"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
    path("edit_post/<int:id>", views.edit_post, name="edit_post")
]