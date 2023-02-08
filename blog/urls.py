from django.urls import path
from django.urls import reverse_lazy
from .views import *


app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("add_post/", PostCreateView.as_view(), name="add_post"),
    path("read_post/<int:pk>", PostDetailView.as_view(), name="read_post"),
    path("delete_post/<int:pk>", PostDeleteView.as_view(), name="delete_post"),
    path("edit_post/<int:pk>", PostUpdateView.as_view(), name="edit_post"),
    path("accounts/login/", BlogLoginView.as_view(), name="login"),  # пишем .as_view потому что это просто класс
    path("accounts/logout/", BlogLogoutView.as_view(), name="logout"),
    path("accounts/sign_up/", sign_up, name="sign_up"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category"),
    path('posts/<int:post_id>/add_like/', add_like, name='add_like'),
    path('posts/<int:post_id>/remove_like/', remove_like, name='remove_like')
]