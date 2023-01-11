from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views  # аутентификация и авторизация пользователя

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add_post/", views.PostCreateView.as_view(), name="add_post"),
    path("read_post/<int:pk>", views.PostDetailView.as_view(), name="read_post"),
    path("delete_post/<int:pk>", views.PostDeleteView.as_view(), name="delete_post"),
    path("edit_post/<int:pk>", views.PostUpdateView.as_view(), name="edit_post"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),  # пишем .as_view потому что это просто класс
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page=reverse_lazy('blog:index')), name="logout"),
    path("accounts/sign_up/", views.sign_up, name="sign_up")
]