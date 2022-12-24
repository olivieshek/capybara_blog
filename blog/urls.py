from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add_post/", views.PostCreateView.as_view(), name="add_post"),
    path("read_post/<int:pk>", views.PostDetailView.as_view(), name="read_post"),
    path("delete_post/<int:pk>", views.PostDeleteView.as_view(), name="delete_post"),
    path("edit_post/<int:pk>", views.PostUpdateView.as_view(), name="edit_post"),
    # path("authorization", views.authorization, name="authorization"),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="blog/authorization.html")),
    # path('logout/', views.logout, name='logout')
]