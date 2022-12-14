from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_post/", views.add_post, name="add_post"),
    path("read_post/<int:id>", views.read_post, name="read_post"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
    path("edit_post/<int:id>", views.edit_post, name="edit_post"),
    path("authorization", views.authorization, name="authorization"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="blog/authorization.html")),
    path('logout/', views.logout, name='logout')
]